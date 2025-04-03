# amds

Developer-friendly & type-safe Python SDK specifically catered to leverage *amds* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=amds&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/american-data-science-jvy/amds). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [amds](https://github.com/americandatascience/amds/blob/master/#amds)
  * [SDK Installation](https://github.com/americandatascience/amds/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/americandatascience/amds/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/americandatascience/amds/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/americandatascience/amds/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/americandatascience/amds/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/americandatascience/amds/blob/master/#retries)
  * [Error Handling](https://github.com/americandatascience/amds/blob/master/#error-handling)
  * [Server Selection](https://github.com/americandatascience/amds/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/americandatascience/amds/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/americandatascience/amds/blob/master/#resource-management)
  * [Debugging](https://github.com/americandatascience/amds/blob/master/#debugging)
* [Development](https://github.com/americandatascience/amds/blob/master/#development)
  * [Maturity](https://github.com/americandatascience/amds/blob/master/#maturity)
  * [Contributions](https://github.com/americandatascience/amds/blob/master/#contributions)
  * [Command Line Interface (CLI)](https://github.com/americandatascience/amds/blob/master/#command-line-interface-cli)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install amds
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add amds
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from amds python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "amds",
# ]
# ///

from amds import Amds

sdk = Amds(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from amds import Amds
import os


with Amds(
    api_key=os.getenv("AMDS_API_KEY", ""),
) as a_client:

    res = a_client.environments.get()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
from amds import Amds
import asyncio
import os

async def main():

    async with Amds(
        api_key=os.getenv("AMDS_API_KEY", ""),
    ) as a_client:

        res = await a_client.environments.get_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type   | Scheme  | Environment Variable |
| --------- | ------ | ------- | -------------------- |
| `api_key` | apiKey | API key | `AMDS_API_KEY`       |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
from amds import Amds
import os


with Amds(
    api_key=os.getenv("AMDS_API_KEY", ""),
) as a_client:

    res = a_client.environments.get()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [alph](https://github.com/americandatascience/amds/blob/master/docs/sdks/alph/README.md)

* [gpt4o_mini](https://github.com/americandatascience/amds/blob/master/docs/sdks/alph/README.md#gpt4o_mini) - gpt-4o-mini
* [gpt4o](https://github.com/americandatascience/amds/blob/master/docs/sdks/alph/README.md#gpt4o) - gpt-4o
* [gpt4](https://github.com/americandatascience/amds/blob/master/docs/sdks/alph/README.md#gpt4) - gpt-4
* [claude35_haiku](https://github.com/americandatascience/amds/blob/master/docs/sdks/alph/README.md#claude35_haiku) - claude-3-5-haiku
* [claude35_sonnet](https://github.com/americandatascience/amds/blob/master/docs/sdks/alph/README.md#claude35_sonnet) - claude-3-5-sonnet


### [compute](https://github.com/americandatascience/amds/blob/master/docs/sdks/compute/README.md)

* [get](https://github.com/americandatascience/amds/blob/master/docs/sdks/compute/README.md#get) - Get Compute

### [environments](https://github.com/americandatascience/amds/blob/master/docs/sdks/environments/README.md)

* [get](https://github.com/americandatascience/amds/blob/master/docs/sdks/environments/README.md#get) - Get Environments

### [integrated_servers](https://github.com/americandatascience/amds/blob/master/docs/sdks/integratedservers/README.md)

* [get](https://github.com/americandatascience/amds/blob/master/docs/sdks/integratedservers/README.md#get) - Get Integrated Servers
* [add](https://github.com/americandatascience/amds/blob/master/docs/sdks/integratedservers/README.md#add) - Add Integrated Server
* [delete](https://github.com/americandatascience/amds/blob/master/docs/sdks/integratedservers/README.md#delete) - Delete Integrated Server

### [servers](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md)

* [get](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md#get) - Get Servers
* [create](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md#create) - Create Server
* [stop](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md#stop) - Stop Server
* [start](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md#start) - Start Server
* [delete](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md#delete) - Delete Server
* [run_code](https://github.com/americandatascience/amds/blob/master/docs/sdks/servers/README.md#run_code) - Run Code

#### [servers.files](https://github.com/americandatascience/amds/blob/master/docs/sdks/files/README.md)

* [get](https://github.com/americandatascience/amds/blob/master/docs/sdks/files/README.md#get) - Get File
* [upload](https://github.com/americandatascience/amds/blob/master/docs/sdks/files/README.md#upload) - Upload File

### [tunnels](https://github.com/americandatascience/amds/blob/master/docs/sdks/tunnels/README.md)

* [get](https://github.com/americandatascience/amds/blob/master/docs/sdks/tunnels/README.md#get) - Get Tunnel
* [create](https://github.com/americandatascience/amds/blob/master/docs/sdks/tunnels/README.md#create) - Create Tunnel
* [delete](https://github.com/americandatascience/amds/blob/master/docs/sdks/tunnels/README.md#delete) - Delete Tunnel

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from amds import Amds
from amds.utils import BackoffStrategy, RetryConfig
import os


with Amds(
    api_key=os.getenv("AMDS_API_KEY", ""),
) as a_client:

    res = a_client.environments.get(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from amds import Amds
from amds.utils import BackoffStrategy, RetryConfig
import os


with Amds(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("AMDS_API_KEY", ""),
) as a_client:

    res = a_client.environments.get()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| models.APIError | 4XX, 5XX    | \*/\*        |

### Example

```python
from amds import Amds, models
import os


with Amds(
    api_key=os.getenv("AMDS_API_KEY", ""),
) as a_client:
    res = None
    try:

        res = a_client.environments.get()

        # Handle response
        print(res)

    except models.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from amds import Amds
import os


with Amds(
    server_url="https://dashboard.amdatascience.com",
    api_key=os.getenv("AMDS_API_KEY", ""),
) as a_client:

    res = a_client.environments.get()

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from amds import Amds
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Amds(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from amds import Amds
from amds.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Amds(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Amds` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from amds import Amds
import os
def main():

    with Amds(
        api_key=os.getenv("AMDS_API_KEY", ""),
    ) as a_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Amds(
        api_key=os.getenv("AMDS_API_KEY", ""),
    ) as a_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from amds import Amds
import logging

logging.basicConfig(level=logging.DEBUG)
s = Amds(debug_logger=logging.getLogger("amds"))
```

You can also enable a default debug logger by setting an environment variable `AMDS_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=amds&utm_campaign=python)

<!-- Start CLI Usage [cli] -->
## Command Line Interface (CLI)

In addition to the SDK, this project includes a command-line interface (CLI) for interacting with the American Data Science API.

### Installation

The CLI is automatically installed when you install the Python package.

```bash
pip install amds
```

### Commands

- `amds environments` - Manage environments
- `amds servers` - Manage servers
- `amds compute` - Manage compute resources
- `amds login` - Authenticate with American Data Science API
- `amds jupyter` - Launch and manage local Jupyter Lab instances

### Jupyter Command

The `jupyter` command allows you to launch a local Jupyter Lab instance with advanced features:

```bash
# Launch a local Jupyter Lab instance with ngrok proxy
amds jupyter launch

# Launch with alph-editor
amds jupyter launch --with-alph

# Specify custom port and directory
amds jupyter launch --port 9999 --directory /path/to/notebooks
```

This command:
- Launches a local Jupyter Lab instance
- Creates a secure public URL using ngrok
- Uploads instance information to dashboard.amdatascience.com
- Can launch with the alph-editor extension

See `amds jupyter launch --help` for all options.
<!-- End CLI Usage [cli] -->
