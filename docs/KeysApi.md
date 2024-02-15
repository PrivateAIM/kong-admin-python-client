# kong_admin_client.KeysApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key**](KeysApi.md#create_key) | **POST** /keys | Create a new Key
[**delete_key**](KeysApi.md#delete_key) | **DELETE** /keys/{key_id_or_name} | Delete a Key
[**get_key**](KeysApi.md#get_key) | **GET** /keys/{key_id_or_name} | Fetch a Key
[**list_key**](KeysApi.md#list_key) | **GET** /keys | List all Keys
[**update_key**](KeysApi.md#update_key) | **PATCH** /keys/{key_id_or_name} | Update a Key
[**upsert_key**](KeysApi.md#upsert_key) | **PUT** /keys/{key_id_or_name} | Upsert a Key


# **create_key**
> Key create_key(create_key_request=create_key_request)

Create a new Key

This API endpoint allows you to create a new key. When the request is successful, the API will respond with a 200 status code and a JSON object that represents the newly created key. If the request is invalid, the API will respond with a `400` status code and an error message in the response body.  > Note: This API is not available in DB-less mode. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_request import CreateKeyRequest
from kong_admin_client.models.key import Key
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
    api_instance = kong_admin_client.KeysApi(api_client)
    create_key_request = kong_admin_client.CreateKeyRequest() # CreateKeyRequest |  (optional)

    try:
        # Create a new Key
        api_response = api_instance.create_key(create_key_request=create_key_request)
        print("The response of KeysApi->create_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysApi->create_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_key_request** | [**CreateKeyRequest**](CreateKeyRequest.md)|  | [optional] 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created Key |  -  |
**400** | Invalid Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> delete_key(key_id_or_name)

Delete a Key

Delete a Key

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
    api_instance = kong_admin_client.KeysApi(api_client)
    key_id_or_name = '24D0DBDA-671C-11ED-BA0B-EF1DCCD3725' # str | The unique identifier or the name of the Key to retrieve.

    try:
        # Delete a Key
        api_instance.delete_key(key_id_or_name)
    except Exception as e:
        print("Exception when calling KeysApi->delete_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id_or_name** | **str**| The unique identifier or the name of the Key to retrieve. | 

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
**204** | Successfully deleted Key or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key**
> Key get_key(key_id_or_name)

Fetch a Key

Get a Key using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.key import Key
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
    api_instance = kong_admin_client.KeysApi(api_client)
    key_id_or_name = '24D0DBDA-671C-11ED-BA0B-EF1DCCD3725' # str | The unique identifier or the name of the Key to retrieve.

    try:
        # Fetch a Key
        api_response = api_instance.get_key(key_id_or_name)
        print("The response of KeysApi->get_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysApi->get_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id_or_name** | **str**| The unique identifier or the name of the Key to retrieve. | 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Key |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key**
> ListKey200Response list_key(size=size, offset=offset, tags=tags)

List all Keys

List all Keys

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_key200_response import ListKey200Response
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
    api_instance = kong_admin_client.KeysApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Keys
        api_response = api_instance.list_key(size=size, offset=offset, tags=tags)
        print("The response of KeysApi->list_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysApi->list_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListKey200Response**](ListKey200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key**
> Key update_key(key_id_or_name, create_key_request=create_key_request)

Update a Key

Update a Key

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_request import CreateKeyRequest
from kong_admin_client.models.key import Key
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
    api_instance = kong_admin_client.KeysApi(api_client)
    key_id_or_name = '24D0DBDA-671C-11ED-BA0B-EF1DCCD3725' # str | The unique identifier or the name of the Key to retrieve.
    create_key_request = kong_admin_client.CreateKeyRequest() # CreateKeyRequest |  (optional)

    try:
        # Update a Key
        api_response = api_instance.update_key(key_id_or_name, create_key_request=create_key_request)
        print("The response of KeysApi->update_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysApi->update_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id_or_name** | **str**| The unique identifier or the name of the Key to retrieve. | 
 **create_key_request** | [**CreateKeyRequest**](CreateKeyRequest.md)|  | [optional] 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Key |  -  |
**400** | Invalid Key |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_key**
> Key upsert_key(key_id_or_name, create_key_request=create_key_request)

Upsert a Key

Create or Update Key using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_request import CreateKeyRequest
from kong_admin_client.models.key import Key
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
    api_instance = kong_admin_client.KeysApi(api_client)
    key_id_or_name = '24D0DBDA-671C-11ED-BA0B-EF1DCCD3725' # str | The unique identifier or the name of the Key to retrieve.
    create_key_request = kong_admin_client.CreateKeyRequest() # CreateKeyRequest |  (optional)

    try:
        # Upsert a Key
        api_response = api_instance.upsert_key(key_id_or_name, create_key_request=create_key_request)
        print("The response of KeysApi->upsert_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeysApi->upsert_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id_or_name** | **str**| The unique identifier or the name of the Key to retrieve. | 
 **create_key_request** | [**CreateKeyRequest**](CreateKeyRequest.md)|  | [optional] 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Key |  -  |
**400** | Invalid Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

