# kong_admin_client.ConsumersApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_consumer**](ConsumersApi.md#create_consumer) | **POST** /consumers | Create a new Consumer
[**delete_consumer**](ConsumersApi.md#delete_consumer) | **DELETE** /consumers/{consumer_username_or_id} | Delete a Consumer
[**get_consumer**](ConsumersApi.md#get_consumer) | **GET** /consumers/{consumer_username_or_id} | Fetch a Consumer
[**list_consumer**](ConsumersApi.md#list_consumer) | **GET** /consumers | List all Consumers
[**update_consumer**](ConsumersApi.md#update_consumer) | **PATCH** /consumers/{consumer_username_or_id} | Update a Consumer
[**upsert_consumer**](ConsumersApi.md#upsert_consumer) | **PUT** /consumers/{consumer_username_or_id} | Update a Consumer


# **create_consumer**
> Consumer create_consumer(create_consumer_request=create_consumer_request)

Create a new Consumer

Create a new Consumer

### Example


```python
import kong_admin_client
from kong_admin_client.models.consumer import Consumer
from kong_admin_client.models.create_consumer_request import CreateConsumerRequest
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
    api_instance = kong_admin_client.ConsumersApi(api_client)
    create_consumer_request = kong_admin_client.CreateConsumerRequest() # CreateConsumerRequest | Consumer request body (optional)

    try:
        # Create a new Consumer
        api_response = api_instance.create_consumer(create_consumer_request=create_consumer_request)
        print("The response of ConsumersApi->create_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumersApi->create_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_consumer_request** | [**CreateConsumerRequest**](CreateConsumerRequest.md)| Consumer request body | [optional] 

### Return type

[**Consumer**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created Consumer |  -  |
**400** | Invalid Consumer |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_consumer**
> delete_consumer(consumer_username_or_id)

Delete a Consumer

Delete a specific consumer from the system using either the consumer ID or the consumer username. This operation is irreversible and permanently removes all data associated with the specified consumer. If the consumer was deleted succesfully the endpoint will return a 204 response indicating that the resource did not exist.

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
    api_instance = kong_admin_client.ConsumersApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.

    try:
        # Delete a Consumer
        api_instance.delete_consumer(consumer_username_or_id)
    except Exception as e:
        print("Exception when calling ConsumersApi->delete_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 

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
**204** | Successfully deleted Consumer or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consumer**
> Consumer get_consumer(consumer_username_or_id)

Fetch a Consumer

Retrieve the details of a specific consumer in the system using either the consumer ID or the consumer username. If the consumer with the specified ID or username cannot be found, the endpoint will return a 404.

### Example


```python
import kong_admin_client
from kong_admin_client.models.consumer import Consumer
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
    api_instance = kong_admin_client.ConsumersApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.

    try:
        # Fetch a Consumer
        api_response = api_instance.get_consumer(consumer_username_or_id)
        print("The response of ConsumersApi->get_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumersApi->get_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 

### Return type

[**Consumer**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Consumer |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_consumer**
> ListConsumer200Response list_consumer(size=size, offset=offset, tags=tags)

List all Consumers

Retrieve a list of all consumers.You can use query parameters to filter the results by size or tags, for example `/consumers?size=50&tags=enterprise`.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_consumer200_response import ListConsumer200Response
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
    api_instance = kong_admin_client.ConsumersApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Consumers
        api_response = api_instance.list_consumer(size=size, offset=offset, tags=tags)
        print("The response of ConsumersApi->list_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumersApi->list_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListConsumer200Response**](ListConsumer200Response.md)

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

# **update_consumer**
> Consumer update_consumer(consumer_username_or_id, create_consumer_request=create_consumer_request)

Update a Consumer

Update the details of a specific consumer in the system using either the consumer ID or the consumer username.If the consumer with the specified ID or username cannot be found, the endpoint will return a 404.

### Example


```python
import kong_admin_client
from kong_admin_client.models.consumer import Consumer
from kong_admin_client.models.create_consumer_request import CreateConsumerRequest
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
    api_instance = kong_admin_client.ConsumersApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    create_consumer_request = kong_admin_client.CreateConsumerRequest() # CreateConsumerRequest | Consumer request body (optional)

    try:
        # Update a Consumer
        api_response = api_instance.update_consumer(consumer_username_or_id, create_consumer_request=create_consumer_request)
        print("The response of ConsumersApi->update_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumersApi->update_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **create_consumer_request** | [**CreateConsumerRequest**](CreateConsumerRequest.md)| Consumer request body | [optional] 

### Return type

[**Consumer**](Consumer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Consumer |  -  |
**400** | Invalid Consumer |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_consumer**
> UpsertConsumer200Response upsert_consumer(consumer_username_or_id, create_consumer_request=create_consumer_request)

Update a Consumer

Create or Update Consumer using ID or username. The consumer will be identified via the username or id attribute.If the consumer with the specified ID or username cannot be found, the endpoint will return a 404.  When the username or id attribute has the structure of a UUID, the Consumer being inserted/replaced will be identified by its id. Otherwise it will be identified by its username.  When creating a new Consumer without specifying id (neither in the URL nor in the body), then it will be auto-generated.  Notice that specifying a username in the URL and a different one in the request body is not allowed.  > Note: This API is not available in DB-less mode.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_consumer_request import CreateConsumerRequest
from kong_admin_client.models.upsert_consumer200_response import UpsertConsumer200Response
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
    api_instance = kong_admin_client.ConsumersApi(api_client)
    consumer_username_or_id = 'my-username' # str | The unique identifier or the username of the Consumer to retrieve.
    create_consumer_request = kong_admin_client.CreateConsumerRequest() # CreateConsumerRequest | Consumer request body (optional)

    try:
        # Update a Consumer
        api_response = api_instance.upsert_consumer(consumer_username_or_id, create_consumer_request=create_consumer_request)
        print("The response of ConsumersApi->upsert_consumer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConsumersApi->upsert_consumer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consumer_username_or_id** | **str**| The unique identifier or the username of the Consumer to retrieve. | 
 **create_consumer_request** | [**CreateConsumerRequest**](CreateConsumerRequest.md)| Consumer request body | [optional] 

### Return type

[**UpsertConsumer200Response**](UpsertConsumer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The consumer object response body |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

