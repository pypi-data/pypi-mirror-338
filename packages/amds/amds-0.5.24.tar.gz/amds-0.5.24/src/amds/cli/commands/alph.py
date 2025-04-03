import click
import os
import sys
import json
import subprocess
import shutil
import tempfile
import webbrowser
import requests
import time
from pathlib import Path
import socket
import random
import string
from urllib.parse import urlparse
import threading
import signal
import hashlib
import re
import queue
from ..utils import print_json


def create_jupyter_config(
    config_dir,
    allow_origin="https://*.amdatascience.com",
    disable_sudo=False,
):
    """
    Create a Jupyter config file with CORS settings

    Args:
        config_dir: Directory to create the config in
        allow_origin: CORS allow-origin setting
        disable_sudo: Whether to disable sudo/root access

    Returns:
        Path to the created config file
    """
    # Create the config directory if it doesn't exist
    os.makedirs(config_dir, exist_ok=True)

    # Create a jupyter_server_config.py file with CORS configuration
    config_file = os.path.join(config_dir, "jupyter_server_config.py")

    sudo_config = ""
    if disable_sudo:
        sudo_config = """
# Disable sudo/root access
c.ServerApp.allow_root = False
c.ServerApp.allow_sudo = False
"""

    with open(config_file, "w") as f:
        f.write(
            f"""
# Configuration file for jupyter-server.

c = get_config()

# Configure CORS settings
c.ServerApp.allow_origin = '{allow_origin}'
c.ServerApp.allow_credentials = True
c.ServerApp.allow_methods = ['*']
c.ServerApp.allow_headers = ['Content-Type', 'Authorization', 'X-Requested-With', 
                            'X-XSRFToken', 'ngrok-skip-browser-warning', 'Origin', 
                            'Accept', 'Cache-Control', 'X-Requested-With', '*']
{sudo_config}
"""
        )

    return config_file


def is_port_in_use(port):
    """Check if a port is already in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


def find_free_port(start_port, max_attempts=10):
    """Find a free port starting from start_port"""
    port = start_port
    attempts = 0

    while attempts < max_attempts:
        if not is_port_in_use(port):
            return port
        port += 1
        attempts += 1

    return None


def check_jupyter_health(jupyter_url, token):
    """Check if Jupyter server is responding properly"""
    try:
        # Extract base URL without token
        base_url = jupyter_url.split("?")[0]
        # Construct the API URL to check server status
        api_url = f"{base_url}/api/status"
        headers = {}
        if token:
            headers["Authorization"] = f"token {token}"

        response = requests.get(api_url, headers=headers, timeout=5)
        return response.status_code == 200
    except Exception:
        return False


def check_tunnel_health(tunnel_url, provider):
    """Check if tunnel is responding properly"""
    try:
        headers = {}
        if provider == "ngrok":
            # Add parameter to bypass ngrok browser warning
            check_url = f"{tunnel_url}?ngrok-skip-browser-warning=true"
            headers["ngrok-skip-browser-warning"] = "true"
        else:
            check_url = tunnel_url

        response = requests.get(check_url, timeout=5, headers=headers)
        return response.status_code < 400
    except Exception:
        return False


def start_jupyter_server(directory, port, jupyter_config):
    """
    Start Jupyter Lab server and extract token

    Returns:
        tuple: (jupyter_process, jupyter_url, token)
    """
    click.echo(f"Starting Jupyter Lab on port {port}...")
    jupyter_cmd = [
        "jupyter",
        "lab",
        f"--port={port}",
        "--no-browser",
        f"--notebook-dir={directory}",
        "--ip=0.0.0.0",
        f"--config={jupyter_config}",
    ]

    # Start Jupyter process
    jupyter_process = subprocess.Popen(
        jupyter_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    # Wait for Jupyter to start and get the token
    token = None
    jupyter_url = None
    for line in iter(jupyter_process.stderr.readline, ""):
        if "http://localhost:" in line or "http://127.0.0.1:" in line:
            # Extract just the URL part, removing the log prefix
            url_part = re.search(r"(http://[^\s]+)", line)
            if url_part:
                jupyter_url = url_part.group(0).strip()
                token = jupyter_url.split("token=")[-1].strip()
                break
            else:
                # Fallback to old method if regex fails
                jupyter_url = line.strip().split("or ")[-1].strip()
                token = jupyter_url.split("token=")[-1].strip()
                break

        sys.stderr.write(line)

        if not token and "ERROR" in line:
            click.secho(
                "Error starting Jupyter Lab. Please check the logs above.",
                fg="red",
                bold=True,
            )
            jupyter_process.terminate()
            sys.exit(1)

    if not token:
        click.secho("Error: Could not get Jupyter token. Exiting.", fg="red", bold=True)
        jupyter_process.terminate()
        sys.exit(1)

    click.secho("✓ Jupyter Lab started successfully", fg="green", bold=True)

    # Short delay to ensure all output is captured
    time.sleep(0.5)

    return jupyter_process, jupyter_url, token


def setup_tunnel(client, port, app_port=None, server_name=None):
    """
    Set up Cloudflare tunnel via API

    Returns:
        dict: Tunnel information or None if failed
    """
    click.secho(
        "Setting up tunnel via API...",
        fg="blue",
        bold=True,
    )
    try:
        with client as c:
            # Call the tunnels API to get a tunnel token
            request_data = {
                "jupyter_port": port,
            }

            # Add app port if specified
            if app_port:
                request_data["app_port"] = app_port

            # Add server name if we want a specific one
            if not server_name:
                server_name = f"local-{int(time.time())}"
            request_data["server_name"] = server_name

            # Call the API to create the tunnel
            try:
                result = c.tunnels.create(request=request_data)

                # Extract tunnel data from the response
                if hasattr(result, "result") and hasattr(result.result, "data"):
                    tunnel_data = result.result.data
                    cloudflare_token = tunnel_data.token
                    tunnel_url = tunnel_data.jupyter_url
                    tunnel_name = tunnel_data.name
                    tunnel_id = getattr(tunnel_data, "id", None)
                    app_tunnel_url = getattr(tunnel_data, "app_url", None)

                    # Install the tunnel service
                    click.secho("Installing tunnel service...", fg="blue")
                    install_cmd = [
                        "sudo",
                        "cloudflared",
                        "service",
                        "install",
                        cloudflare_token,
                    ]

                    # Run the install command
                    subprocess.run(install_cmd, check=True)
                    click.secho(
                        "✓ tunnel service installed",
                        fg="green",
                        bold=True,
                    )

                    return {
                        "tunnel_url": tunnel_url,
                        "app_tunnel_url": app_tunnel_url,
                        "cloudflare_token": cloudflare_token,
                        "tunnel_name": tunnel_name,
                        "tunnel_id": tunnel_id,
                    }
                else:
                    click.secho(
                        "Warning: Invalid response from tunnels API.",
                        fg="yellow",
                    )
                    return None

            except Exception as e:
                click.secho(
                    f"Error creating tunnel: {str(e)}",
                    fg="yellow",
                )
                return None
    except Exception as e:
        click.secho(f"Error setting up tunnel: {str(e)}", fg="yellow")
        return None


def setup_temporary_tunnel(port, app_port=None):
    """
    Set up temporary Cloudflare tunnel

    Returns:
        dict: Tunnel information
    """
    # Start Cloudflare tunnel
    click.secho(
        f"Starting temporary tunnel to port {port}...",
        fg="blue",
        bold=True,
    )
    cloudflare_cmd = [
        "cloudflared",
        "tunnel",
        "--url",
        f"http://localhost:{port}",
    ]

    tunnel_process = subprocess.Popen(
        cloudflare_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    # Wait for cloudflare tunnel to start and get the public URL
    tunnel_url = None
    app_tunnel_url = None
    app_tunnel_process = None

    # Define reader function for output stream
    def reader(stream, queue):
        for line in iter(stream.readline, ""):
            queue.put(line)
        stream.close()

    # Create a queue for the output lines
    output_queue = queue.Queue()

    # Start reader threads for both stdout and stderr
    threading.Thread(
        target=reader, args=(tunnel_process.stdout, output_queue), daemon=True
    ).start()
    threading.Thread(
        target=reader, args=(tunnel_process.stderr, output_queue), daemon=True
    ).start()

    # Process the output lines to find tunnel URL
    tunnel_url = find_tunnel_url(output_queue, tunnel_process)

    if not tunnel_url:
        click.secho(
            "Error: Could not get tunnel URL. Exiting.",
            fg="red",
            bold=True,
        )
        click.echo(
            "Try running 'cloudflared tunnel --url http://localhost:8888' manually to check for errors."
        )
        tunnel_process.terminate()
        return None

    click.secho(f"Tunnel created at {tunnel_url}", fg="green")

    # Start additional tunnel for app port if specified
    if app_port:
        app_tunnel_url, app_tunnel_process = setup_app_tunnel(app_port)

    return {
        "tunnel_url": tunnel_url,
        "tunnel_process": tunnel_process,
        "app_tunnel_url": app_tunnel_url,
        "app_tunnel_process": app_tunnel_process,
    }


def find_tunnel_url(output_queue, process, timeout=60):
    """Extract tunnel URL from process output queue"""
    tunnel_url = None
    start_time = time.time()

    while time.time() < start_time + timeout:
        try:
            # Get line with timeout to avoid blocking forever
            line = output_queue.get(timeout=1)
            sys.stdout.write(line)

            # Look for the cloudflare tunnel URL
            if "https://" in line and "trycloudflare.com" in line:
                match = re.search(r"https://[^\s|]+", line)
                if match:
                    tunnel_url = match.group(0).strip()
                    break

            # Also check for URLs without table formatting
            if "https://" in line:
                match = re.search(r"https://[^ |\n\r]+\.trycloudflare\.com", line)
                if match:
                    tunnel_url = match.group(0).strip()
                    break

            if "error" in line.lower():
                click.echo("Error starting tunnel. Please check the logs above.")
                process.terminate()
                return None

        except queue.Empty:
            # No output for a second, check if process is still alive
            if process.poll() is not None:
                # Process has ended
                break
            continue

    return tunnel_url


def setup_app_tunnel(app_port):
    """Set up additional tunnel for application port"""
    click.secho(
        f"Starting additional tunnel for application port {app_port}...",
        fg="blue",
        bold=True,
    )
    app_cloudflare_cmd = [
        "cloudflared",
        "tunnel",
        "--url",
        f"http://localhost:{app_port}",
    ]

    app_tunnel_process = subprocess.Popen(
        app_cloudflare_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    # Create a queue for the output lines
    app_output_queue = queue.Queue()

    # Define reader function
    def reader(stream, queue):
        for line in iter(stream.readline, ""):
            queue.put(line)
        stream.close()

    # Start reader threads for app tunnel
    threading.Thread(
        target=reader,
        args=(app_tunnel_process.stdout, app_output_queue),
        daemon=True,
    ).start()
    threading.Thread(
        target=reader,
        args=(app_tunnel_process.stderr, app_output_queue),
        daemon=True,
    ).start()

    app_tunnel_url = find_tunnel_url(app_output_queue, app_tunnel_process)

    if app_tunnel_url:
        click.secho(
            f"Additional tunnel for app port created at {app_tunnel_url}",
            fg="green",
        )
    else:
        click.secho(
            "Warning: Could not create additional tunnel for app port. Continuing without app tunnel.",
            fg="yellow",
        )

    return app_tunnel_url, app_tunnel_process


def register_with_dashboard(
    client,
    server_name,
    token,
    tunnel_url,
    app_tunnel_url=None,
    app_port=None,
    thumbnail=None,
):
    """
    Register server with dashboard

    Returns:
        str: Registered server name or None if failed
    """
    click.echo("Uploading information to dashboard.amdatascience.com...")

    try:
        with client as c:
            # Format data according to the expected API format
            try:
                # Add the integrated server using the proper API method
                request_data = {
                    "environment": "local",
                    "server_name": server_name,
                    "token": token,
                    "url": tunnel_url,
                }

                # Add app port forward URL if available
                if app_tunnel_url:
                    request_data["port_forward_url"] = app_tunnel_url

                # Add the app port number if available
                if app_port:
                    request_data["port"] = app_port

                # Add custom thumbnail if provided, otherwise use default
                if thumbnail:
                    request_data["thumb"] = thumbnail
                else:
                    # Use Jupyter's favicon as default thumbnail
                    request_data["thumb"] = f"/images/compute_icons/amds.svg"

                # Get the API key from the client or environment
                api_key_to_use = get_api_key_from_client(client)

                if api_key_to_use:
                    from amds import Amds

                    fresh_client = Amds(api_key=api_key_to_use)
                    # Call the add method directly with the fresh client
                    result = fresh_client.integrated_servers.add(request=request_data)
                else:
                    click.echo(
                        "Falling back to original client for server registration"
                    )
                    # Try the original client but with explicit request parameter
                    result = c.integrated_servers.add(request=request_data)

                click.secho(f"Server registered as '{server_name}'", fg="green")
                dashboard_url = "https://dashboard.amdatascience.com"
                click.echo(
                    f"View in dashboard: {click.style(dashboard_url, fg='bright_blue')}"
                )
                return server_name

            except Exception as e:
                click.echo(f"Warning: Could not register with dashboard: {str(e)}")
                try:
                    # Try alternative method as last resort - direct call
                    result = c.integrated_servers.add(**request_data)
                    return server_name
                except:
                    return None
    except Exception as e:
        click.echo(f"Warning: Failed to connect to dashboard: {str(e)}")
        return None


def get_api_key_from_client(client):
    """Extract API key from client object"""
    if hasattr(client, "api_key"):
        return client.api_key
    elif hasattr(client, "sdk_configuration") and hasattr(
        client.sdk_configuration, "security"
    ):
        return client.sdk_configuration.security.api_key
    elif hasattr(client, "_api_key"):
        return client._api_key
    else:
        return os.environ.get("AMDS_API_KEY")


def cleanup_cloudflare_service():
    """Uninstall Cloudflare tunnel service"""
    try:
        click.echo("Uninstalling tunnel service...")
        # Run the uninstall command (this may need sudo)
        subprocess.run(["sudo", "cloudflared", "service", "uninstall"], check=False)
    except Exception as e:
        click.echo(f"Warning: Failed to uninstall tunnel service: {str(e)}")
        click.echo(
            "You may need to manually uninstall it with: sudo cloudflared service uninstall"
        )


def cleanup_tunnel_api(client, tunnel_id, api_key=None):
    """Clean up Cloudflare tunnel via API"""
    click.echo(f"Cleaning up tunnel via API...")
    try:
        # Import the SDK if needed
        from amds import Amds

        # Get the API key - prioritize the directly provided one
        cleanup_api_key = api_key or get_api_key_from_client(client)

        if cleanup_api_key:
            # Create a new client without using a context manager
            cleanup_client = Amds(api_key=cleanup_api_key)
            # Call delete tunnel API
            try:
                result = cleanup_client.tunnels.delete(tunnel_id=tunnel_id)
                click.echo(f"Tunnel with ID '{tunnel_id}' deleted")
            except Exception as e1:
                click.echo(f"Tunnel deletion failed: {str(e1)}")
                click.echo("The tunnel may need to be manually removed.")
        else:
            click.echo(
                "Warning: No API key available for tunnel cleanup. The tunnel may need to be manually removed."
            )
    except Exception as e:
        click.echo(f"Warning: Failed to connect to API for tunnel cleanup: {str(e)}")


def cleanup_dashboard_integration(client, registered_server_name, api_key=None):
    """Clean up dashboard integration by deleting the server record"""
    click.echo(f"Cleaning up dashboard integration...")
    try:
        # Import the SDK if needed
        from amds import Amds

        # Get the API key - prioritize the directly provided one
        cleanup_api_key = api_key or get_api_key_from_client(client)

        if cleanup_api_key:
            # Create a new client without using a context manager
            cleanup_client = Amds(api_key=cleanup_api_key)
            # Call delete directly without using a context manager
            try:
                result = cleanup_client.integrated_servers.delete(
                    server_name=registered_server_name
                )
                click.echo(
                    f"Server '{registered_server_name}' unregistered from dashboard"
                )
            except Exception as e1:
                click.echo(f"Deletion failed: {str(e1)}")
                click.echo(
                    "The server may need to be manually removed from the dashboard."
                )
        else:
            click.echo(
                "Warning: No API key available for cleanup. The server may need to be manually removed."
            )
    except Exception as e:
        click.echo(f"Warning: Failed to connect to dashboard for cleanup: {str(e)}")


def start_health_check_thread(jupyter_url, token, tunnel_url, app_tunnel_url=None):
    """Start a thread to periodically check health of services"""

    def health_checker():
        """Periodically check if services are still running"""
        while True:
            time.sleep(30)  # Check every 30 seconds
            try:
                # Check if Jupyter is still responsive
                if not check_jupyter_health(jupyter_url, token):
                    click.secho(
                        "Warning: Jupyter server is not responding! The application may be experiencing issues.",
                        fg="yellow",
                        bold=True,
                    )

                # Check if tunnel is still connected
                if not check_tunnel_health(tunnel_url, "cloudflare"):
                    click.secho(
                        "Warning: Tunnel may be down! Public URL may not be accessible.",
                        fg="yellow",
                        bold=True,
                    )

                # Check app tunnel health if it exists
                if app_tunnel_url and not check_tunnel_health(
                    app_tunnel_url, "cloudflare"
                ):
                    click.secho(
                        "Warning: App tunnel may be down! App URL may not be accessible.",
                        fg="yellow",
                        bold=True,
                    )
            except Exception as e:
                # Log exceptions but don't crash the monitoring thread
                click.secho(
                    f"Warning: Health check encountered an error: {str(e)}",
                    fg="yellow",
                )

    # Start health check in a daemon thread
    health_thread = threading.Thread(target=health_checker, daemon=True)
    health_thread.start()
    return health_thread


def display_output(
    output_format,
    jupyter_url,
    tunnel_url,
    token,
    app_tunnel_url=None,
    registered_server_name=None,
    cloudflare_token=None,
):
    """Display output information based on user preference"""
    if output_format == "standard":
        click.echo("\n" + "=" * 60)
        click.secho("Alph Editor is connected with local server", fg="green", bold=True)
        click.echo("=" * 60)
        click.echo("Local URL:        " + click.style(jupyter_url, fg="bright_blue"))
        click.echo("Public URL:       " + click.style(tunnel_url, fg="bright_blue"))
        if app_tunnel_url:
            click.echo(
                "App URL:          " + click.style(app_tunnel_url, fg="bright_blue")
            )
        if registered_server_name:
            alph_url = f"https://dashboard.amdatascience.com/alph-editor/{registered_server_name}"
            click.echo("Alph Editor URL:  " + click.style(alph_url, fg="bright_blue"))
        click.echo("=" * 60)
        click.echo("\nPress Ctrl+C to stop the server...\n")
    elif output_format == "minimal":
        click.echo("Local URL:        " + jupyter_url)
        click.echo("Public URL:       " + tunnel_url)
        if app_tunnel_url:
            click.echo("App URL:          " + app_tunnel_url)
        if registered_server_name:
            alph_url = f"https://dashboard.amdatascience.com/alph-editor/{registered_server_name}"
            click.echo("Alph Editor URL:  " + alph_url)
        click.echo("\nPress Ctrl+C to stop the server...")
    elif output_format == "json":
        output = {
            "local_url": jupyter_url,
            "public_url": tunnel_url,
            "token": token,
        }
        if app_tunnel_url:
            output["app_url"] = app_tunnel_url
        if registered_server_name:
            output["alph_url"] = (
                f"https://dashboard.amdatascience.com/alph-editor/{registered_server_name}"
            )
            output["server_name"] = registered_server_name
        if cloudflare_token:
            output["cloudflare_token"] = cloudflare_token
        print_json(output)


@click.group()
def alph():
    """Launch Alph Editor from your local machine"""
    pass


@alph.command("launch")
@click.option("--port", type=int, default=8888, help="Port to run Jupyter Lab on")
@click.option("--no-browser", is_flag=True, help="Don't open browser automatically")
@click.option(
    "--directory", type=str, default=".", help="Directory to launch Jupyter Lab in"
)
@click.option(
    "--app-port",
    type=int,
    default=5000,
    help="Additional port to tunnel for your application (stored as port_forward_url)",
)
@click.option(
    "--api-key", envvar="AMDS_API_KEY", help="API key for dashboard integration"
)
@click.option("--allow-origin", type=str, default="*", help="CORS allow-origin setting")
@click.option(
    "--disable-sudo", is_flag=True, help="Disable sudo/root permissions in the notebook"
)
@click.option(
    "--output-format",
    type=click.Choice(["standard", "minimal", "json"]),
    default="standard",
    help="Output format for command results",
)
@click.option(
    "--thumbnail",
    type=str,
    default=None,
    help="Custom thumbnail URL for dashboard display",
)
@click.option(
    "--use-temp-tunnel",
    is_flag=True,
    help="Use temporary cloudflared tunnel instead of service",
)
@click.pass_obj
def launch_jupyter(
    client,
    port,
    no_browser,
    directory,
    app_port,
    api_key,
    allow_origin,
    disable_sudo,
    output_format,
    thumbnail,
    use_temp_tunnel,
):
    """Launch Alph Editor powered by your local Jupyter Lab server with Cloudflare proxy."""

    # Check prerequisites
    import shutil

    if not shutil.which("jupyter"):
        click.secho(
            "Error: Jupyter Lab is not installed. Please install it with:", fg="red"
        )
        click.echo("    pip install jupyterlab")
        sys.exit(1)

    if not shutil.which("cloudflared"):
        click.secho(
            "Error: cloudflared is not installed. Please install it from https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/",
            fg="red",
        )
        sys.exit(1)

    # Check if port is in use and find an alternative if needed
    if is_port_in_use(port):
        click.secho(f"Warning: Port {port} is already in use.", fg="yellow")
        new_port = find_free_port(port + 1)
        if new_port:
            click.secho(f"Using alternative port {new_port} instead.", fg="yellow")
            port = new_port
        else:
            click.secho(
                "Error: Could not find an available port. Please specify a different port with --port.",
                fg="red",
            )
            sys.exit(1)

    # If app_port is specified, check if it's in use
    app_tunnel_url = None
    if app_port:
        if is_port_in_use(app_port):
            click.secho(f"Warning: App port {app_port} is already in use.", fg="yellow")
            new_app_port = find_free_port(app_port + 1)
            if new_app_port:
                click.secho(
                    f"Using alternative app port {new_app_port} instead.", fg="yellow"
                )
                app_port = new_app_port
            else:
                click.secho(
                    "Error: Could not find an available app port. Please specify a different port with --app-port.",
                    fg="red",
                )
                sys.exit(1)

    # Create a temporary directory for Jupyter config
    jupyter_dir = tempfile.mkdtemp(prefix="jupyter-amds-")

    try:
        # Create Jupyter config with CORS settings
        config_file = create_jupyter_config(jupyter_dir, allow_origin, disable_sudo)
        click.secho(
            f"Created Jupyter config with CORS allow-origin: {allow_origin}", fg="blue"
        )
        if disable_sudo:
            click.echo(
                "Root/sudo permissions have been disabled in the notebook server"
            )

        # Start Jupyter Lab process
        jupyter_process, jupyter_url, token = start_jupyter_server(
            directory, port, config_file
        )

        # Variables to store tunnel information
        tunnel_url = None
        app_tunnel_url = None
        cloudflare_token = None
        tunnel_process = None
        app_tunnel_process = None
        tunnel_name = None

        # Initialize client if needed
        if not client and api_key:
            from amds import Amds

            client = Amds(api_key=api_key)

        # Handle the tunneling - either tunnel or temporary
        if not use_temp_tunnel and (api_key or client):
            # Try to use the tunnel via API
            tunnel_info = setup_tunnel(client, port, app_port)

            if tunnel_info:
                tunnel_url = tunnel_info["tunnel_url"]
                app_tunnel_url = tunnel_info["app_tunnel_url"]
                cloudflare_token = tunnel_info["cloudflare_token"]
                tunnel_name = tunnel_info["tunnel_name"]
                tunnel_id = tunnel_info.get("tunnel_id")
                tunnel_name_for_dashboard = tunnel_name
            else:
                click.secho("Falling back to temporary tunnel...", fg="yellow")
                use_temp_tunnel = True
        else:
            # If requested or if we don't have API access, use temporary tunnel
            use_temp_tunnel = True

        # Set up temporary tunnel if needed
        if use_temp_tunnel:
            tunnel_info = setup_temporary_tunnel(port, app_port)

            if tunnel_info:
                tunnel_url = tunnel_info["tunnel_url"]
                tunnel_process = tunnel_info["tunnel_process"]
                app_tunnel_url = tunnel_info["app_tunnel_url"]
                app_tunnel_process = tunnel_info["app_tunnel_process"]
            else:
                jupyter_process.terminate()
                sys.exit(1)

        # Upload information to dashboard.amdatascience.com if we have an API key
        registered_server_name = None
        if api_key or client:
            if "tunnel_name_for_dashboard" in locals() and tunnel_name_for_dashboard:
                # Use the name from the tunnel API if available
                server_name = tunnel_name_for_dashboard
            else:
                # Generate a new server name
                server_name = f"local-{int(time.time())}"

            registered_server_name = register_with_dashboard(
                client,
                server_name,
                token,
                tunnel_url,
                app_tunnel_url,
                app_port,
                thumbnail,
            )
        else:
            click.echo(
                "Note: No API key provided. Running without dashboard integration."
            )

        # Open browser if requested
        if not no_browser:
            if registered_server_name:
                full_url = f"https://dashboard.amdatascience.com/alph-editor/{registered_server_name}"
            else:
                full_url = f"{jupyter_url}"

            click.echo(f"Opening browser at {full_url}")
            webbrowser.open(full_url)

        # Display information to user
        display_output(
            output_format,
            jupyter_url,
            tunnel_url,
            token,
            app_tunnel_url,
            registered_server_name,
            cloudflare_token if not use_temp_tunnel else None,
        )

        # Start health check thread
        health_thread = start_health_check_thread(
            jupyter_url, token, tunnel_url, app_tunnel_url
        )

        # Keep the process running until user interrupts
        try:
            jupyter_process.wait()
        except KeyboardInterrupt:
            click.secho("Shutting down...", fg="yellow")
        except Exception as e:
            click.secho(f"Error: {str(e)}", fg="red")
        finally:
            # Clean up processes
            try:
                jupyter_process.terminate()
                click.echo("Jupyter server stopped.")
            except Exception:
                pass

            try:
                if tunnel_process:
                    tunnel_process.terminate()
                    click.echo("Temporary tunnel closed.")
            except Exception:
                pass

            # Clean up app tunnel process if it exists
            if app_port and app_tunnel_process:
                try:
                    app_tunnel_process.terminate()
                    click.echo("Temporary app tunnel closed.")
                except Exception:
                    pass

            # If we used the tunnel service, try to clean it up
            if not use_temp_tunnel and cloudflare_token:
                cleanup_cloudflare_service()
                # Also clean up the tunnel on Cloudflare's side
                if tunnel_id and (api_key or client):
                    cleanup_tunnel_api(client, tunnel_id, api_key)

            # Delete the integrated server record if it was registered
            if registered_server_name and (api_key or client):
                cleanup_dashboard_integration(client, registered_server_name, api_key)

    except Exception as e:
        click.echo(f"Error: {str(e)}")
        sys.exit(1)
    finally:
        # Clean up temporary directory
        try:
            import shutil

            shutil.rmtree(jupyter_dir)
        except Exception:
            pass
