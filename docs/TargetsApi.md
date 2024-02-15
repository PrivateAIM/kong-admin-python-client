# kong_admin_client.TargetsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_target_for_upstream**](TargetsApi.md#create_target_for_upstream) | **POST** /upstreams/{upstream_id_or_name}/targets | Create a new Target associated with an Upstream
[**delete_upstream_target**](TargetsApi.md#delete_upstream_target) | **DELETE** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Delete a Target associated with a an Upstream
[**fetch_target_for_upstream**](TargetsApi.md#fetch_target_for_upstream) | **GET** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Fetch a Target associated with an Upstream
[**list_targets_for_upstream**](TargetsApi.md#list_targets_for_upstream) | **GET** /upstreams/{upstream_id_or_name}/targets | List all Targets associated with an Upstream
[**update_target_for_upstream**](TargetsApi.md#update_target_for_upstream) | **PATCH** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Update a target associated with an Upstream
[**upsert_target_for_upstream**](TargetsApi.md#upsert_target_for_upstream) | **PUT** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Upsert a Target associated with an Upstream


# **create_target_for_upstream**
> Target create_target_for_upstream(upstream_id_or_name, create_target_for_upstream_request=create_target_for_upstream_request)

Create a new Target associated with an Upstream

Create a new Target associated with an Upstream

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_target_for_upstream_request import CreateTargetForUpstreamRequest
from kong_admin_client.models.target import Target
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
    api_instance = kong_admin_client.TargetsApi(api_client)
    upstream_id_or_name = 'upstream_id_or_name_example' # str | ID or name of the related Upstream
    create_target_for_upstream_request = {"upstream":{"id":"173a6cee-90d1-40a7-89cf-0329eca780a6"},"weight":100,"tags":["string"]} # CreateTargetForUpstreamRequest |  (optional)

    try:
        # Create a new Target associated with an Upstream
        api_response = api_instance.create_target_for_upstream(upstream_id_or_name, create_target_for_upstream_request=create_target_for_upstream_request)
        print("The response of TargetsApi->create_target_for_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetsApi->create_target_for_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| ID or name of the related Upstream | 
 **create_target_for_upstream_request** | [**CreateTargetForUpstreamRequest**](CreateTargetForUpstreamRequest.md)|  | [optional] 

### Return type

[**Target**](Target.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created Target |  -  |
**400** | Invalid Target |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upstream_target**
> delete_upstream_target(upstream_id_or_name, target_id_or_target)

Delete a Target associated with a an Upstream

Delete a Target associated with a an Upstream using ID or target.

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
    api_instance = kong_admin_client.TargetsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.
    target_id_or_target = 'example.com:8000' # str | The host/port combination element of the target to set as unhealthy, or the `id` of an existing target entry.

    try:
        # Delete a Target associated with a an Upstream
        api_instance.delete_upstream_target(upstream_id_or_name, target_id_or_target)
    except Exception as e:
        print("Exception when calling TargetsApi->delete_upstream_target: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 
 **target_id_or_target** | **str**| The host/port combination element of the target to set as unhealthy, or the &#x60;id&#x60; of an existing target entry. | 

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
**204** | Successfully deleted Target or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_target_for_upstream**
> Target fetch_target_for_upstream(upstream_id_or_name, target_id_or_target)

Fetch a Target associated with an Upstream

Get a Target associated with an Upstream using ID or target.

### Example


```python
import kong_admin_client
from kong_admin_client.models.target import Target
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
    api_instance = kong_admin_client.TargetsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.
    target_id_or_target = 'example.com:8000' # str | The host/port combination element of the target to set as unhealthy, or the `id` of an existing target entry.

    try:
        # Fetch a Target associated with an Upstream
        api_response = api_instance.fetch_target_for_upstream(upstream_id_or_name, target_id_or_target)
        print("The response of TargetsApi->fetch_target_for_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetsApi->fetch_target_for_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 
 **target_id_or_target** | **str**| The host/port combination element of the target to set as unhealthy, or the &#x60;id&#x60; of an existing target entry. | 

### Return type

[**Target**](Target.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Target |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_targets_for_upstream**
> ListTargetsForUpstream200Response list_targets_for_upstream(upstream_id_or_name, size=size, offset=offset, tags=tags)

List all Targets associated with an Upstream

List all Targets associated with a an Upstream

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_targets_for_upstream200_response import ListTargetsForUpstream200Response
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
    api_instance = kong_admin_client.TargetsApi(api_client)
    upstream_id_or_name = 'upstream_id_or_name_example' # str | ID or name of the related Upstream
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Targets associated with an Upstream
        api_response = api_instance.list_targets_for_upstream(upstream_id_or_name, size=size, offset=offset, tags=tags)
        print("The response of TargetsApi->list_targets_for_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetsApi->list_targets_for_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| ID or name of the related Upstream | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListTargetsForUpstream200Response**](ListTargetsForUpstream200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Targets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_target_for_upstream**
> Target update_target_for_upstream(upstream_id_or_name, target_id_or_target, create_target_for_upstream_request=create_target_for_upstream_request)

Update a target associated with an Upstream

Update a Target associated with a an Upstream using ID or target.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_target_for_upstream_request import CreateTargetForUpstreamRequest
from kong_admin_client.models.target import Target
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
    api_instance = kong_admin_client.TargetsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.
    target_id_or_target = 'example.com:8000' # str | The host/port combination element of the target to set as unhealthy, or the `id` of an existing target entry.
    create_target_for_upstream_request = {"upstream":{"id":"173a6cee-90d1-40a7-89cf-0329eca780a6"},"weight":100,"tags":["string"]} # CreateTargetForUpstreamRequest |  (optional)

    try:
        # Update a target associated with an Upstream
        api_response = api_instance.update_target_for_upstream(upstream_id_or_name, target_id_or_target, create_target_for_upstream_request=create_target_for_upstream_request)
        print("The response of TargetsApi->update_target_for_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetsApi->update_target_for_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 
 **target_id_or_target** | **str**| The host/port combination element of the target to set as unhealthy, or the &#x60;id&#x60; of an existing target entry. | 
 **create_target_for_upstream_request** | [**CreateTargetForUpstreamRequest**](CreateTargetForUpstreamRequest.md)|  | [optional] 

### Return type

[**Target**](Target.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Target |  -  |
**400** | Invalid Target |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_target_for_upstream**
> Target upsert_target_for_upstream(upstream_id_or_name, target_id_or_target, create_target_for_upstream_request=create_target_for_upstream_request)

Upsert a Target associated with an Upstream

Create or Update a Target associated with an Upstream using ID or target.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_target_for_upstream_request import CreateTargetForUpstreamRequest
from kong_admin_client.models.target import Target
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
    api_instance = kong_admin_client.TargetsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.
    target_id_or_target = 'example.com:8000' # str | The host/port combination element of the target to set as unhealthy, or the `id` of an existing target entry.
    create_target_for_upstream_request = {"upstream":{"id":"173a6cee-90d1-40a7-89cf-0329eca780a6"},"weight":100,"tags":["string"]} # CreateTargetForUpstreamRequest |  (optional)

    try:
        # Upsert a Target associated with an Upstream
        api_response = api_instance.upsert_target_for_upstream(upstream_id_or_name, target_id_or_target, create_target_for_upstream_request=create_target_for_upstream_request)
        print("The response of TargetsApi->upsert_target_for_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TargetsApi->upsert_target_for_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 
 **target_id_or_target** | **str**| The host/port combination element of the target to set as unhealthy, or the &#x60;id&#x60; of an existing target entry. | 
 **create_target_for_upstream_request** | [**CreateTargetForUpstreamRequest**](CreateTargetForUpstreamRequest.md)|  | [optional] 

### Return type

[**Target**](Target.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Target |  -  |
**400** | Invalid Target |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

