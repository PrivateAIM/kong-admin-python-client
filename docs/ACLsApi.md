# kong_admin_client.ACLsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_acl_for_consumer**](ACLsApi.md#create_acl_for_consumer) | **POST** /consumers/{consumer_username_or_id}/acls | Create a new ACL associated with a Consumer
[**list_acls_for_consumer**](ACLsApi.md#list_acls_for_consumer) | **GET** /consumers/{consumer_username_or_id}/acls | List all ACLs associated with a consumer


# **create_acl_for_consumer**
> ACL create_acl_for_consumer(consumer_username_or_id, create_acl_for_consumer_request=create_acl_for_consumer_request)

Create a new ACL associated with a Consumer

Create a new ACL associated with a Consumer

### Example


```python
import kong_admin_client
from kong_admin_client.models.acl import ACL
from kong_admin_client.models.create_acl_for_consumer_request import CreateAclForConsumerRequest
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
    api_instance = kong_admin_client.ACLsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    create_acl_for_consumer_request = kong_admin_client.CreateAclForConsumerRequest() # CreateAclForConsumerRequest | ACL request body (optional)

    try:
        # Create a new ACL associated with a Consumer
        api_response = api_instance.create_acl_for_consumer(consumer_username_or_id, create_acl_for_consumer_request=create_acl_for_consumer_request)
        print("The response of ACLsApi->create_acl_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLsApi->create_acl_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **create_acl_for_consumer_request** | [**CreateAclForConsumerRequest**](CreateAclForConsumerRequest.md)| ACL request body | [optional] 

### Return type

[**ACL**](ACL.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created ACL |  -  |
**400** | Invalid ACL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_acls_for_consumer**
> ListAclsForConsumer200Response list_acls_for_consumer(consumer_username_or_id, size=size, offset=offset, tags=tags)

List all ACLs associated with a consumer

Retrieve a list of all ACLs associated with a consumer.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_acls_for_consumer200_response import ListAclsForConsumer200Response
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
    api_instance = kong_admin_client.ACLsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all ACLs associated with a consumer
        api_response = api_instance.list_acls_for_consumer(consumer_username_or_id, size=size, offset=offset, tags=tags)
        print("The response of ACLsApi->list_acls_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ACLsApi->list_acls_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListAclsForConsumer200Response**](ListAclsForConsumer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Consumers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

