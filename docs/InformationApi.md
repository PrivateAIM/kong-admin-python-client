# kong_admin_client.InformationApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_endpoints**](InformationApi.md#get_endpoints) | **GET** /endpoints | List all endpoints
[**get_schemas_entity**](InformationApi.md#get_schemas_entity) | **GET** /schemas/{entity}/validate | Retrieve entity schema
[**get_schemas_filters_filter_name**](InformationApi.md#get_schemas_filters_filter_name) | **GET** /schemas/filters/{filter_name} | Retrieve Proxy-Wasm Filter JSON Schema
[**get_schemas_plugins_plugin_name**](InformationApi.md#get_schemas_plugins_plugin_name) | **GET** /schemas/plugins/{plugin_name} | Retrieve Plugin Schema
[**get_schemas_vaults_vault_name**](InformationApi.md#get_schemas_vaults_vault_name) | **GET** /schemas/vaults/{vault_name} | Retrieve Vault Schema
[**get_status**](InformationApi.md#get_status) | **GET** /status | Health Routes
[**get_timers**](InformationApi.md#get_timers) | **GET** /timers | Retrieve Runtime Debugging Info of Kong&#39;s Timers
[**head_endpoints**](InformationApi.md#head_endpoints) | **HEAD** /{endpoint} | Check endpoint or entity existence
[**options_endpoint**](InformationApi.md#options_endpoint) | **OPTIONS** /{endpoint} | List method by endpoint
[**post_schemas_entity_validate**](InformationApi.md#post_schemas_entity_validate) | **POST** /schemas/{entity}/validate | Validate a configuration against a schema
[**post_schemas_plugins_validate**](InformationApi.md#post_schemas_plugins_validate) | **POST** /schemas/plugins/validate | Validate plugin schema


# **get_endpoints**
> GetEndpoints200Response get_endpoints()

List all endpoints

List all available endpoints provided by the Admin API.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_endpoints200_response import GetEndpoints200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)

    try:
        # List all endpoints
        api_response = api_instance.get_endpoints()
        print("The response of InformationApi->get_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->get_endpoints: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetEndpoints200Response**](GetEndpoints200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas_entity**
> GetSchemasEntity200Response get_schemas_entity(entity)

Retrieve entity schema

Retrieve the schema of an entity. This is useful to understand what fields an entity accepts, and can be used for building third-party integrations with Kong.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_schemas_entity200_response import GetSchemasEntity200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Retrieve entity schema
        api_response = api_instance.get_schemas_entity(entity)
        print("The response of InformationApi->get_schemas_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->get_schemas_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 

### Return type

[**GetSchemasEntity200Response**](GetSchemasEntity200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas_filters_filter_name**
> object get_schemas_filters_filter_name(filter_name)

Retrieve Proxy-Wasm Filter JSON Schema

Retrieve the JSON Schema of a Proxy-Wasm filter's configuration. This is useful to understand what fields a filter accepts, and can be used for building third-party integrations to the Kong's filter chain system. 

### Example


```python
import kong_admin_client
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    filter_name = 'go-rate-limiting' # str | The name of a Proxy-Wasm filter

    try:
        # Retrieve Proxy-Wasm Filter JSON Schema
        api_response = api_instance.get_schemas_filters_filter_name(filter_name)
        print("The response of InformationApi->get_schemas_filters_filter_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->get_schemas_filters_filter_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| The name of a Proxy-Wasm filter | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas_plugins_plugin_name**
> get_schemas_plugins_plugin_name(plugin_name)

Retrieve Plugin Schema

Retrieve the schema of a plugin's configuration. This is useful to understand what fields a plugin accepts, and can be used for building third-party integrations to the Kong's plugin system. 

### Example


```python
import kong_admin_client
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    plugin_name = 'basic-auth' # str | The name of a Kong plugin

    try:
        # Retrieve Plugin Schema
        api_instance.get_schemas_plugins_plugin_name(plugin_name)
    except Exception as e:
        print("Exception when calling InformationApi->get_schemas_plugins_plugin_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_name** | **str**| The name of a Kong plugin | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schemas_vaults_vault_name**
> Vault get_schemas_vaults_vault_name(vault_name)

Retrieve Vault Schema

Retrieve the schema of a vault.

### Example


```python
import kong_admin_client
from kong_admin_client.models.vault import Vault
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    vault_name = 'vault_name_example' # str | The vault schema to be returned

    try:
        # Retrieve Vault Schema
        api_response = api_instance.get_schemas_vaults_vault_name(vault_name)
        print("The response of InformationApi->get_schemas_vaults_vault_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->get_schemas_vaults_vault_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_name** | **str**| The vault schema to be returned | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | No vault named |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> GetStatus200Response get_status()

Health Routes

Retrieve usage information about a node, with some basic information about the connections being processed by the underlying nginx process, the status of the database connection, and node's memory usage.  If you want to monitor the Kong process, since Kong is built on top of nginx, every existing nginx monitoring tool or agent can be used.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_status200_response import GetStatus200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)

    try:
        # Health Routes
        api_response = api_instance.get_status()
        print("The response of InformationApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatus200Response**](GetStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timers**
> GetTimers200Response get_timers()

Retrieve Runtime Debugging Info of Kong's Timers

Retrieve runtime stats data from [lua-resty-timer-ng](https://github.com/Kong/lua-resty-timer-ng).

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_timers200_response import GetTimers200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)

    try:
        # Retrieve Runtime Debugging Info of Kong's Timers
        api_response = api_instance.get_timers()
        print("The response of InformationApi->get_timers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->get_timers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTimers200Response**](GetTimers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_endpoints**
> head_endpoints(endpoint)

Check endpoint or entity existence

Similar to `HTTP` GET, but does not return the body. Returns HTTP 200 when the endpoint exits or HTTP 404 when it does not. Other status codes are possible. 

### Example


```python
import kong_admin_client
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    endpoint = 'key' # str | Any available endpoint

    try:
        # Check endpoint or entity existence
        api_instance.head_endpoints(endpoint)
    except Exception as e:
        print("Exception when calling InformationApi->head_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Any available endpoint | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date - The date and time at which the message was originated <br>  * Content-Type - The media type of the message content <br>  * Connection - Indicates whether the connection will be closed after the message is completed <br>  * Access-Control-Allow-Origin - Indicates whether the resource can be accessed by any origin <br>  * X-Kong-Admin-Request-ID - A unique identifier for the request, generated by Kong <br>  * X-Kong-Admin-Latency - The time taken to process the request on the server, in milliseconds <br>  * Server - The software used by the origin server to handle the request <br>  |
**404** | Endpoint does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **options_endpoint**
> options_endpoint(endpoint)

List method by endpoint

List all the supported HTTP methods by an endpoint. This can also be used with a CORS preflight request. 

### Example


```python
import kong_admin_client
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    endpoint = 'key' # str | Any available endpoint

    try:
        # List method by endpoint
        api_instance.options_endpoint(endpoint)
    except Exception as e:
        print("Exception when calling InformationApi->options_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**| Any available endpoint | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * Date - The date and time at which the message was originated <br>  * Connection - Indicates whether the connection will be closed after the message is completed <br>  * Access-Control-Allow-Origin - Indicates whether the resource can be accessed by any origin <br>  * Access-Control-Allow-Headers - Used in response to a preflight request to indicate which HTTP headers can be used during the actual request <br>  * X-Kong-Admin-Request-ID - A unique identifier for the request, generated by Kong <br>  * Allow - Lists the HTTP methods that are supported for the resource <br>  * Access-Control-Allow-Methods - Indicates the methods allowed when accessing the resource in response to a preflight request <br>  * X-Kong-Admin-Latency - The time taken to process the request on the server, in milliseconds <br>  * Server - The software used by the origin server to handle the request <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schemas_entity_validate**
> PostSchemasEntityValidate200Response post_schemas_entity_validate(entity)

Validate a configuration against a schema

Check validity of a configuration against its entity schema. This allows you to test your input before submitting a request to the entity endpoints of the Admin API.  A requests to the entity endpoint using the given configuration may still fail due to other reasons, such as invalid foreign key relationships or uniqueness check failures against the contents of the data store.

### Example


```python
import kong_admin_client
from kong_admin_client.models.post_schemas_entity_validate200_response import PostSchemasEntityValidate200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)
    entity = 'entity_example' # str | 

    try:
        # Validate a configuration against a schema
        api_response = api_instance.post_schemas_entity_validate(entity)
        print("The response of InformationApi->post_schemas_entity_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->post_schemas_entity_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity** | **str**|  | 

### Return type

[**PostSchemasEntityValidate200Response**](PostSchemasEntityValidate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_schemas_plugins_validate**
> PostSchemasPluginsValidate200Response post_schemas_plugins_validate()

Validate plugin schema

Check validity of a plugin configuration against the plugins entity schema. This allows you to test your input before submitting a request to the entity endpoints of the Admin API.   This only performs the schema validation checks, checking that the input configuration is well-formed. A requests to the entity endpoint using the given configuration may still fail due to other reasons, such as invalid foreign key relationships or uniqueness check failures against the contents of the data store.

### Example


```python
import kong_admin_client
from kong_admin_client.models.post_schemas_plugins_validate200_response import PostSchemasPluginsValidate200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.InformationApi(api_client)

    try:
        # Validate plugin schema
        api_response = api_instance.post_schemas_plugins_validate()
        print("The response of InformationApi->post_schemas_plugins_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InformationApi->post_schemas_plugins_validate: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PostSchemasPluginsValidate200Response**](PostSchemasPluginsValidate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

