# kong_admin_client.KeyAuthsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_auth_for_consumer**](KeyAuthsApi.md#create_key_auth_for_consumer) | **POST** /consumers/{consumer_username_or_id}/key-auth | Create a new Key-auth associated with a Consumer
[**list_key_auths_for_consumer**](KeyAuthsApi.md#list_key_auths_for_consumer) | **GET** /consumers/{consumer_username_or_id}/key-auth | List all Key-auths associated with a consumer


# **create_key_auth_for_consumer**
> KeyAuth create_key_auth_for_consumer(consumer_username_or_id, create_key_auth_for_consumer_request=create_key_auth_for_consumer_request)

Create a new Key-auth associated with a Consumer

Create a new Key-auth associated with a Consumer

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_auth_for_consumer_request import CreateKeyAuthForConsumerRequest
from kong_admin_client.models.key_auth import KeyAuth
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
    api_instance = kong_admin_client.KeyAuthsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    create_key_auth_for_consumer_request = kong_admin_client.CreateKeyAuthForConsumerRequest() # CreateKeyAuthForConsumerRequest | key-auth request body (optional)

    try:
        # Create a new Key-auth associated with a Consumer
        api_response = api_instance.create_key_auth_for_consumer(consumer_username_or_id, create_key_auth_for_consumer_request=create_key_auth_for_consumer_request)
        print("The response of KeyAuthsApi->create_key_auth_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthsApi->create_key_auth_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **create_key_auth_for_consumer_request** | [**CreateKeyAuthForConsumerRequest**](CreateKeyAuthForConsumerRequest.md)| key-auth request body | [optional] 

### Return type

[**KeyAuth**](KeyAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created Key-auth |  -  |
**400** | Invalid Key-auth |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_auths_for_consumer**
> ListKeyAuthsForConsumer200Response list_key_auths_for_consumer(consumer_username_or_id, size=size, offset=offset, tags=tags)

List all Key-auths associated with a consumer

Retrieve a list of all Key-auths associated with a consumer.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_key_auths_for_consumer200_response import ListKeyAuthsForConsumer200Response
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
    api_instance = kong_admin_client.KeyAuthsApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Key-auths associated with a consumer
        api_response = api_instance.list_key_auths_for_consumer(consumer_username_or_id, size=size, offset=offset, tags=tags)
        print("The response of KeyAuthsApi->list_key_auths_for_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeyAuthsApi->list_key_auths_for_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListKeyAuthsForConsumer200Response**](ListKeyAuthsForConsumer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Key-auths |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

