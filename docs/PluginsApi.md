# kong_admin_client.PluginsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plugin**](PluginsApi.md#create_plugin) | **POST** /plugins | Create a new Plugin
[**create_plugin_for_consumer**](PluginsApi.md#create_plugin_for_consumer) | **POST** /consumers/{consumer_username_or_id}/plugins | Create a new Plugin associated with a Consumer
[**create_plugin_for_route**](PluginsApi.md#create_plugin_for_route) | **POST** /routes/{route_id_or_name}/plugins | Create a new Plugin associated with a route
[**create_plugin_for_service**](PluginsApi.md#create_plugin_for_service) | **POST** /services/{service_id_or_name}plugins | Create a new Plugin associated with a service
[**delete_plugin**](PluginsApi.md#delete_plugin) | **DELETE** /plugins/{plugin_id} | Delete a Plugin
[**delete_plugin_for_a_service**](PluginsApi.md#delete_plugin_for_a_service) | **DELETE** /services/{service_id_or_name}/plugins/{plugin_id} | Delete a plugin associated with a service
[**delete_plugin_for_consumer**](PluginsApi.md#delete_plugin_for_consumer) | **DELETE** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Delete a Plugin associated with a Consumer
[**delete_plugin_for_route**](PluginsApi.md#delete_plugin_for_route) | **DELETE** /routes/{route_id_or_name}/plugins/{plugin_id} | Delete a Plugin associated with a route
[**fetch_plugin_for_consumer**](PluginsApi.md#fetch_plugin_for_consumer) | **GET** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Fetch a Plugin associated with a Consumer
[**fetch_plugin_for_route**](PluginsApi.md#fetch_plugin_for_route) | **GET** /routes/{route_id_or_name}/plugins/{plugin_id} | Fetch a Plugin associated with a route
[**fetch_plugin_with_a_service**](PluginsApi.md#fetch_plugin_with_a_service) | **GET** /services/{service_id_or_name}/plugins/{plugin_id} | Fetch a Plugin associated with a service
[**get_plugin**](PluginsApi.md#get_plugin) | **GET** /plugins/{plugin_id} | Fetch a Plugin
[**get_plugins_for_service**](PluginsApi.md#get_plugins_for_service) | **GET** /services/{service_id_or_name}plugins | List all Plugins associated with a service
[**list_plugin**](PluginsApi.md#list_plugin) | **GET** /plugins | List all Plugins
[**list_plugins_for_consumer**](PluginsApi.md#list_plugins_for_consumer) | **GET** /consumers/{consumer_username_or_id}/plugins | List all plugins associated with a consumer
[**list_plugins_for_route**](PluginsApi.md#list_plugins_for_route) | **GET** /routes/{route_id_or_name}/plugins | List all Plugins associated with a route
[**update_plugin**](PluginsApi.md#update_plugin) | **PATCH** /plugins/{plugin_id} | Update a Plugin
[**update_plugin_for_a_service**](PluginsApi.md#update_plugin_for_a_service) | **PATCH** /services/{service_id_or_name}/plugins/{plugin_id} | Update a plugin associated with a service
[**update_plugin_for_consumer**](PluginsApi.md#update_plugin_for_consumer) | **PATCH** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Update a Plugin associated with a Consumer
[**update_plugin_for_route**](PluginsApi.md#update_plugin_for_route) | **PATCH** /routes/{route_id_or_name}/plugins/{plugin_id} | Update a Plugin associated with a route
[**upsert_plugin**](PluginsApi.md#upsert_plugin) | **PUT** /plugins/{plugin_id} | Upsert a Plugin
[**upsert_plugin_for_a_service**](PluginsApi.md#upsert_plugin_for_a_service) | **PUT** /services/{service_id_or_name}/plugins/{plugin_id} | Upsert a plugin associated with a service
[**upsert_plugin_for_consumer**](PluginsApi.md#upsert_plugin_for_consumer) | **PUT** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Upsert a Plugin associated with a Consumer
[**upsert_plugin_for_route**](PluginsApi.md#upsert_plugin_for_route) | **PUT** /routes/{route_id_or_name}/plugins/{plugin_id} | Upsert a Plugin associated with a route


# **create_plugin**
> Plugin create_plugin(create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Create a new Plugin

Create a new Plugin  >Note: This API is not available in DB-less mode.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Create a new Plugin
        api_response = api_instance.create_plugin(create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->create_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->create_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_for_consumer**
> Plugin create_plugin_for_consumer(consumer_username_or_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Create a new Plugin associated with a Consumer

Create a new Plugin associated with a Consumer

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Create a new Plugin associated with a Consumer
        api_response = api_instance.create_plugin_for_consumer(consumer_username_or_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->create_plugin_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->create_plugin_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_for_route**
> Plugin create_plugin_for_route(route_id_or_name, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Create a new Plugin associated with a route

Create a new Plugin associated with a route

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Create a new Plugin associated with a route
        api_response = api_instance.create_plugin_for_route(route_id_or_name, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->create_plugin_for_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->create_plugin_for_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_plugin_for_service**
> Plugin create_plugin_for_service(service_id_or_name, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Create a new Plugin associated with a service

Create a new Plugin associated with a service

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Create a new Plugin associated with a service
        api_response = api_instance.create_plugin_for_service(service_id_or_name, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->create_plugin_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->create_plugin_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin**
> delete_plugin(plugin_id)

Delete a Plugin

Delete a Plugin

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
    api_instance = kong_admin_client.PluginsApi(api_client)
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Delete a Plugin
        api_instance.delete_plugin(plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->delete_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

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
**204** | Successfully deleted Plugin or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_for_a_service**
> delete_plugin_for_a_service(service_id_or_name, plugin_id)

Delete a plugin associated with a service

Delete a Plugin associated with a service using ID.

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
    api_instance = kong_admin_client.PluginsApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Delete a plugin associated with a service
        api_instance.delete_plugin_for_a_service(service_id_or_name, plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->delete_plugin_for_a_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

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
**204** | Successfully deleted Plugin or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_for_consumer**
> delete_plugin_for_consumer(consumer_username_or_id, plugin_id)

Delete a Plugin associated with a Consumer

Delete a Plugin associated with a Consumer using ID.

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
    api_instance = kong_admin_client.PluginsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Delete a Plugin associated with a Consumer
        api_instance.delete_plugin_for_consumer(consumer_username_or_id, plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->delete_plugin_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

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
**204** | Successfully deleted Plugin or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_plugin_for_route**
> delete_plugin_for_route(route_id_or_name, plugin_id)

Delete a Plugin associated with a route

Delete a Plugin associated with a route using ID.

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
    api_instance = kong_admin_client.PluginsApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Delete a Plugin associated with a route
        api_instance.delete_plugin_for_route(route_id_or_name, plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->delete_plugin_for_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

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
**204** | Successfully deleted Plugin or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_plugin_for_consumer**
> Plugin fetch_plugin_for_consumer(consumer_username_or_id, plugin_id)

Fetch a Plugin associated with a Consumer

Get a Plugin associated with a Consumer using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Fetch a Plugin associated with a Consumer
        api_response = api_instance.fetch_plugin_for_consumer(consumer_username_or_id, plugin_id)
        print("The response of PluginsApi->fetch_plugin_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->fetch_plugin_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_plugin_for_route**
> Plugin fetch_plugin_for_route(route_id_or_name, plugin_id)

Fetch a Plugin associated with a route

Get a Plugin associated with a route using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Fetch a Plugin associated with a route
        api_response = api_instance.fetch_plugin_for_route(route_id_or_name, plugin_id)
        print("The response of PluginsApi->fetch_plugin_for_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->fetch_plugin_for_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_plugin_with_a_service**
> Plugin fetch_plugin_with_a_service(service_id_or_name, plugin_id)

Fetch a Plugin associated with a service

Get a Plugin associated with a service using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Fetch a Plugin associated with a service
        api_response = api_instance.fetch_plugin_with_a_service(service_id_or_name, plugin_id)
        print("The response of PluginsApi->fetch_plugin_with_a_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->fetch_plugin_with_a_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin**
> Plugin get_plugin(plugin_id)

Fetch a Plugin

Get a Plugin using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.

    try:
        # Fetch a Plugin
        api_response = api_instance.get_plugin(plugin_id)
        print("The response of PluginsApi->get_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_for_service**
> ListPluginsForRoute200Response get_plugins_for_service(service_id_or_name, size=size, offset=offset, tags=tags)

List all Plugins associated with a service

List all Plugins associated with a service

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_plugins_for_route200_response import ListPluginsForRoute200Response
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Plugins associated with a service
        api_response = api_instance.get_plugins_for_service(service_id_or_name, size=size, offset=offset, tags=tags)
        print("The response of PluginsApi->get_plugins_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugins_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListPluginsForRoute200Response**](ListPluginsForRoute200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Plugins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plugin**
> ListPluginsForConsumer200Response list_plugin(size=size, offset=offset, tags=tags)

List all Plugins

This endpoint allows you to list all the plugins. You can use query parameters to filter the results by size or tags, for example `/plugins?size=50&tags=enterprise`.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_plugins_for_consumer200_response import ListPluginsForConsumer200Response
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Plugins
        api_response = api_instance.list_plugin(size=size, offset=offset, tags=tags)
        print("The response of PluginsApi->list_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListPluginsForConsumer200Response**](ListPluginsForConsumer200Response.md)

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

# **list_plugins_for_consumer**
> ListPluginsForConsumer200Response list_plugins_for_consumer(consumer_username_or_id, size=size, offset=offset, tags=tags)

List all plugins associated with a consumer

Retrieve a list of all plugins associated with a consumer.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_plugins_for_consumer200_response import ListPluginsForConsumer200Response
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all plugins associated with a consumer
        api_response = api_instance.list_plugins_for_consumer(consumer_username_or_id, size=size, offset=offset, tags=tags)
        print("The response of PluginsApi->list_plugins_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_plugins_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListPluginsForConsumer200Response**](ListPluginsForConsumer200Response.md)

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

# **list_plugins_for_route**
> ListPluginsForRoute200Response list_plugins_for_route(route_id_or_name, size=size, offset=offset, tags=tags)

List all Plugins associated with a route

List all Plugins associated with a route

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_plugins_for_route200_response import ListPluginsForRoute200Response
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Plugins associated with a route
        api_response = api_instance.list_plugins_for_route(route_id_or_name, size=size, offset=offset, tags=tags)
        print("The response of PluginsApi->list_plugins_for_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->list_plugins_for_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListPluginsForRoute200Response**](ListPluginsForRoute200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Plugins |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin**
> Plugin update_plugin(plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Update a Plugin

Update a Plugin

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Update a Plugin
        api_response = api_instance.update_plugin(plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->update_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->update_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Plugin |  -  |
**400** | Invalid Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_for_a_service**
> Plugin update_plugin_for_a_service(service_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Update a plugin associated with a service

Update a Plugin associated with a service using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Update a plugin associated with a service
        api_response = api_instance.update_plugin_for_a_service(service_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->update_plugin_for_a_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->update_plugin_for_a_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Plugin |  -  |
**400** | Invalid Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_for_consumer**
> ListPluginsForConsumer200Response update_plugin_for_consumer(consumer_username_or_id, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Update a Plugin associated with a Consumer

Update a Plugin associated with a consumer using the consumer username or ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.list_plugins_for_consumer200_response import ListPluginsForConsumer200Response
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Update a Plugin associated with a Consumer
        api_response = api_instance.update_plugin_for_consumer(consumer_username_or_id, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->update_plugin_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->update_plugin_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**ListPluginsForConsumer200Response**](ListPluginsForConsumer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |
**400** | Invalid Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_for_route**
> Plugin update_plugin_for_route(route_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Update a Plugin associated with a route

Update a Plugin associated with a route using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Update a Plugin associated with a route
        api_response = api_instance.update_plugin_for_route(route_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->update_plugin_for_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->update_plugin_for_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Plugin |  -  |
**400** | Invalid Plugin |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_plugin**
> Plugin upsert_plugin(plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Upsert a Plugin

Create or Update Plugin using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Upsert a Plugin
        api_response = api_instance.upsert_plugin(plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->upsert_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->upsert_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_plugin_for_a_service**
> Plugin upsert_plugin_for_a_service(service_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Upsert a plugin associated with a service

Create or Update a Plugin associated with a service using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Upsert a plugin associated with a service
        api_response = api_instance.upsert_plugin_for_a_service(service_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->upsert_plugin_for_a_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->upsert_plugin_for_a_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_plugin_for_consumer**
> ListPluginsForConsumer200Response upsert_plugin_for_consumer(consumer_username_or_id, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Upsert a Plugin associated with a Consumer

Create or Update a Plugin associated with a Consumer using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.list_plugins_for_consumer200_response import ListPluginsForConsumer200Response
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Upsert a Plugin associated with a Consumer
        api_response = api_instance.upsert_plugin_for_consumer(consumer_username_or_id, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->upsert_plugin_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->upsert_plugin_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**ListPluginsForConsumer200Response**](ListPluginsForConsumer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_plugin_for_route**
> Plugin upsert_plugin_for_route(route_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)

Upsert a Plugin associated with a route

Create or Update a Plugin associated with a route using ID.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest
from kong_admin_client.models.plugin import Plugin
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
    api_instance = kong_admin_client.PluginsApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    plugin_id = 'response-ratelimiting' # str | The unique identifier of the Plugin to create or update.
    create_plugin_for_consumer_request = {"name":"rate-limiting","route":"string","service":"string","consumer":"string","instance_name":"rate-limiting-foo","config":{"hour":500,"minute":500},"protocols":["http"],"enabled":true,"tags":["string"],"ordering":{"before":["string"]}} # CreatePluginForConsumerRequest | Plugin request body (optional)

    try:
        # Upsert a Plugin associated with a route
        api_response = api_instance.upsert_plugin_for_route(route_id_or_name, plugin_id, create_plugin_for_consumer_request=create_plugin_for_consumer_request)
        print("The response of PluginsApi->upsert_plugin_for_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->upsert_plugin_for_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **plugin_id** | **str**| The unique identifier of the Plugin to create or update. | 
 **create_plugin_for_consumer_request** | [**CreatePluginForConsumerRequest**](CreatePluginForConsumerRequest.md)| Plugin request body | [optional] 

### Return type

[**Plugin**](Plugin.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Plugin |  -  |
**400** | Invalid Plugin |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

