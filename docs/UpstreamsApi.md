# kong_admin_client.UpstreamsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upstream**](UpstreamsApi.md#create_upstream) | **POST** /upstreams | Create a new Upstream
[**delete_upstream**](UpstreamsApi.md#delete_upstream) | **DELETE** /upstreams/{upstream_id_or_name} | Delete an Upstream
[**get_upstream**](UpstreamsApi.md#get_upstream) | **GET** /upstreams/{upstream_id_or_name} | Fetch an Upstream
[**list_upstream**](UpstreamsApi.md#list_upstream) | **GET** /upstreams | List all Upstreams
[**update_upstream**](UpstreamsApi.md#update_upstream) | **PATCH** /upstreams/{upstream_id_or_name} | Update an Upstream
[**upsert_upstream**](UpstreamsApi.md#upsert_upstream) | **PUT** /upstreams/{upstream_id_or_name} | Update an Upstream


# **create_upstream**
> Upstream create_upstream(create_upstream_request=create_upstream_request)

Create a new Upstream

Create a new Upstream 

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_upstream_request import CreateUpstreamRequest
from kong_admin_client.models.upstream import Upstream
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
    api_instance = kong_admin_client.UpstreamsApi(api_client)
    create_upstream_request = {"name":"my-upstream","algorithm":"round-robin","hash_on":"none","hash_fallback":"none","hash_on_cookie_path":"/","slots":10000,"healthchecks":{"passive":{"type":"http","healthy":{"http_statuses":[200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308],"successes":0},"unhealthy":{"http_statuses":[429,500,503],"timeouts":0,"http_failures":0,"tcp_failures":0}},"active":{"https_verify_certificate":true,"healthy":{"http_statuses":[200,302],"successes":0,"interval":0},"unhealthy":{"http_failures":0,"http_statuses":[429,404,500,501,502,503,504,505],"timeouts":0,"tcp_failures":0,"interval":0},"type":"http","concurrency":10,"headers":{"type":"object","properties":{"x-my-header":{"type":"array","items":{"type":"string"},"description":"The value(s) of the x-my-header header."},"x-another-header":{"type":"array","items":{"type":"string"},"description":"The value(s) of the x-another-header header."}}},"timeout":1,"http_path":"/","https_sni":"example.com"},"threshold":0},"tags":["user-level","low-priority"],"host_header":"example.com","client_certificate":{"id":"ea29aaa3-3b2d-488c-b90c-56df8e0dd8c6"},"use_srv_name":false} # CreateUpstreamRequest |  (optional)

    try:
        # Create a new Upstream
        api_response = api_instance.create_upstream(create_upstream_request=create_upstream_request)
        print("The response of UpstreamsApi->create_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamsApi->create_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_upstream_request** | [**CreateUpstreamRequest**](CreateUpstreamRequest.md)|  | [optional] 

### Return type

[**Upstream**](Upstream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Upstream |  -  |
**400** | Invalid Upstream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_upstream**
> delete_upstream(upstream_id_or_name)

Delete an Upstream

Delete an Upstream

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
    api_instance = kong_admin_client.UpstreamsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.

    try:
        # Delete an Upstream
        api_instance.delete_upstream(upstream_id_or_name)
    except Exception as e:
        print("Exception when calling UpstreamsApi->delete_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 

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
**204** | Successfully deleted Upstream or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upstream**
> Upstream get_upstream(upstream_id_or_name)

Fetch an Upstream

Get an Upstream using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.upstream import Upstream
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
    api_instance = kong_admin_client.UpstreamsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.

    try:
        # Fetch an Upstream
        api_response = api_instance.get_upstream(upstream_id_or_name)
        print("The response of UpstreamsApi->get_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamsApi->get_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 

### Return type

[**Upstream**](Upstream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Upstream |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_upstream**
> ListUpstream200Response list_upstream(size=size, offset=offset, tags=tags)

List all Upstreams

List all registered upstreams. You can filter the results by pagination size, offset, or tags like `/upstreams?size=10&offset=0`. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_upstream200_response import ListUpstream200Response
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
    api_instance = kong_admin_client.UpstreamsApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Upstreams
        api_response = api_instance.list_upstream(size=size, offset=offset, tags=tags)
        print("The response of UpstreamsApi->list_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamsApi->list_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListUpstream200Response**](ListUpstream200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Upstreams |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_upstream**
> Upstream update_upstream(upstream_id_or_name, create_upstream_request=create_upstream_request)

Update an Upstream

Update an Upstream

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_upstream_request import CreateUpstreamRequest
from kong_admin_client.models.upstream import Upstream
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
    api_instance = kong_admin_client.UpstreamsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.
    create_upstream_request = {"name":"my-upstream","algorithm":"round-robin","hash_on":"none","hash_fallback":"none","hash_on_cookie_path":"/","slots":10000,"healthchecks":{"passive":{"type":"http","healthy":{"http_statuses":[200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308],"successes":0},"unhealthy":{"http_statuses":[429,500,503],"timeouts":0,"http_failures":0,"tcp_failures":0}},"active":{"https_verify_certificate":true,"healthy":{"http_statuses":[200,302],"successes":0,"interval":0},"unhealthy":{"http_failures":0,"http_statuses":[429,404,500,501,502,503,504,505],"timeouts":0,"tcp_failures":0,"interval":0},"type":"http","concurrency":10,"headers":{"type":"object","properties":{"x-my-header":{"type":"array","items":{"type":"string"},"description":"The value(s) of the x-my-header header."},"x-another-header":{"type":"array","items":{"type":"string"},"description":"The value(s) of the x-another-header header."}}},"timeout":1,"http_path":"/","https_sni":"example.com"},"threshold":0},"tags":["user-level","low-priority"],"host_header":"example.com","client_certificate":{"id":"ea29aaa3-3b2d-488c-b90c-56df8e0dd8c6"},"use_srv_name":false} # CreateUpstreamRequest |  (optional)

    try:
        # Update an Upstream
        api_response = api_instance.update_upstream(upstream_id_or_name, create_upstream_request=create_upstream_request)
        print("The response of UpstreamsApi->update_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamsApi->update_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 
 **create_upstream_request** | [**CreateUpstreamRequest**](CreateUpstreamRequest.md)|  | [optional] 

### Return type

[**Upstream**](Upstream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Upstream |  -  |
**400** | Invalid Upstream |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_upstream**
> Upstream upsert_upstream(upstream_id_or_name, create_upstream_request=create_upstream_request)

Update an Upstream

Create or Update Upstream using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_upstream_request import CreateUpstreamRequest
from kong_admin_client.models.upstream import Upstream
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
    api_instance = kong_admin_client.UpstreamsApi(api_client)
    upstream_id_or_name = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier or the name of the Upstream associated to the Certificate to be retrieved.
    create_upstream_request = {"name":"my-upstream","algorithm":"round-robin","hash_on":"none","hash_fallback":"none","hash_on_cookie_path":"/","slots":10000,"healthchecks":{"passive":{"type":"http","healthy":{"http_statuses":[200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308],"successes":0},"unhealthy":{"http_statuses":[429,500,503],"timeouts":0,"http_failures":0,"tcp_failures":0}},"active":{"https_verify_certificate":true,"healthy":{"http_statuses":[200,302],"successes":0,"interval":0},"unhealthy":{"http_failures":0,"http_statuses":[429,404,500,501,502,503,504,505],"timeouts":0,"tcp_failures":0,"interval":0},"type":"http","concurrency":10,"headers":{"type":"object","properties":{"x-my-header":{"type":"array","items":{"type":"string"},"description":"The value(s) of the x-my-header header."},"x-another-header":{"type":"array","items":{"type":"string"},"description":"The value(s) of the x-another-header header."}}},"timeout":1,"http_path":"/","https_sni":"example.com"},"threshold":0},"tags":["user-level","low-priority"],"host_header":"example.com","client_certificate":{"id":"ea29aaa3-3b2d-488c-b90c-56df8e0dd8c6"},"use_srv_name":false} # CreateUpstreamRequest |  (optional)

    try:
        # Update an Upstream
        api_response = api_instance.upsert_upstream(upstream_id_or_name, create_upstream_request=create_upstream_request)
        print("The response of UpstreamsApi->upsert_upstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UpstreamsApi->upsert_upstream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upstream_id_or_name** | **str**| The unique identifier or the name of the Upstream associated to the Certificate to be retrieved. | 
 **create_upstream_request** | [**CreateUpstreamRequest**](CreateUpstreamRequest.md)|  | [optional] 

### Return type

[**Upstream**](Upstream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Upstream |  -  |
**400** | Invalid Upstream |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

