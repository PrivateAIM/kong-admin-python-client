# kong_admin_client.KeySetsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_key_set**](KeySetsApi.md#create_key_set) | **POST** /key-sets | Create a new Key-set
[**delete_key_set**](KeySetsApi.md#delete_key_set) | **DELETE** /key-sets/{key-set_id_or_name} | Delete a Key-set
[**get_key_set**](KeySetsApi.md#get_key_set) | **GET** /key-sets/{key-set_id_or_name} | Fetch a Key-set
[**list_key_set**](KeySetsApi.md#list_key_set) | **GET** /key-sets | List all Key-sets
[**update_key_set**](KeySetsApi.md#update_key_set) | **PATCH** /key-sets/{key-set_id_or_name} | Update a Key-set
[**upsert_key_set**](KeySetsApi.md#upsert_key_set) | **PUT** /key-sets/{key-set_id_or_name} | Update a Key-set


# **create_key_set**
> ListKeySet200Response create_key_set(create_key_set_request=create_key_set_request)

Create a new Key-set

This endpoint allows creating a new Key-set by sending a JSON object that describes the Key-set to be created.The request body must contain all the fields required to create a new Key-set.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_set_request import CreateKeySetRequest
from kong_admin_client.models.list_key_set200_response import ListKeySet200Response
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
    api_instance = kong_admin_client.KeySetsApi(api_client)
    create_key_set_request = kong_admin_client.CreateKeySetRequest() # CreateKeySetRequest |  (optional)

    try:
        # Create a new Key-set
        api_response = api_instance.create_key_set(create_key_set_request=create_key_set_request)
        print("The response of KeySetsApi->create_key_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeySetsApi->create_key_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_key_set_request** | [**CreateKeySetRequest**](CreateKeySetRequest.md)|  | [optional] 

### Return type

[**ListKeySet200Response**](ListKeySet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key set object response body |  -  |
**400** | Returned if the request contains invalid data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_set**
> delete_key_set(key_set_id_or_name)

Delete a Key-set

Delete a Key-set  > Note: This API is not available in DB-less mode.

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
    api_instance = kong_admin_client.KeySetsApi(api_client)
    key_set_id_or_name = '46CA83EE-671C-11ED-BFAB-2FE47512C77A' # str | The unique identifier or the `name` attribute of the Key Set that should be associated to the newly-created Key.

    try:
        # Delete a Key-set
        api_instance.delete_key_set(key_set_id_or_name)
    except Exception as e:
        print("Exception when calling KeySetsApi->delete_key_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_set_id_or_name** | **str**| The unique identifier or the &#x60;name&#x60; attribute of the Key Set that should be associated to the newly-created Key. | 

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
**204** | Successfully deleted Key-set or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key_set**
> ListKeySet200Response get_key_set(key_set_id_or_name)

Fetch a Key-set

This endpoint retrieves information about a specific key-set based on its ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_key_set200_response import ListKeySet200Response
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
    api_instance = kong_admin_client.KeySetsApi(api_client)
    key_set_id_or_name = '46CA83EE-671C-11ED-BFAB-2FE47512C77A' # str | The unique identifier or the `name` attribute of the Key Set that should be associated to the newly-created Key.

    try:
        # Fetch a Key-set
        api_response = api_instance.get_key_set(key_set_id_or_name)
        print("The response of KeySetsApi->get_key_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeySetsApi->get_key_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_set_id_or_name** | **str**| The unique identifier or the &#x60;name&#x60; attribute of the Key Set that should be associated to the newly-created Key. | 

### Return type

[**ListKeySet200Response**](ListKeySet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key set object response body |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_key_set**
> ListKeySet200Response list_key_set(size=size, offset=offset, tags=tags)

List all Key-sets

Retrieve a list of all Key-sets in the system. A Key Set object holds a collection of asymmetric key objects. This entity allows to logically group keys by their purpose. Key Sets can be both tagged and filtered by tags. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_key_set200_response import ListKeySet200Response
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
    api_instance = kong_admin_client.KeySetsApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Key-sets
        api_response = api_instance.list_key_set(size=size, offset=offset, tags=tags)
        print("The response of KeySetsApi->list_key_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeySetsApi->list_key_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListKeySet200Response**](ListKeySet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key set object response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key_set**
> ListKeySet200Response update_key_set(key_set_id_or_name, create_key_set_request=create_key_set_request)

Update a Key-set

Update a Key-set using ID or name.  > Note: This API is not available in DB-less mode.  Inserts (or replaces) the Key Set under the requested resource with the definition specified in the body. The Key Set will be identified via the name or id attribute.  When the name or id attribute has the structure of a UUID, the Key Set being inserted/replaced will be identified by its id. Otherwise it will be identified by its name.  When creating a new Key Set without specifying id (neither in the URL nor in the body), then it will be auto-generated.  Notice that specifying a name in the URL and a different one in the request body is not allowed.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_set_request import CreateKeySetRequest
from kong_admin_client.models.list_key_set200_response import ListKeySet200Response
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
    api_instance = kong_admin_client.KeySetsApi(api_client)
    key_set_id_or_name = '46CA83EE-671C-11ED-BFAB-2FE47512C77A' # str | The unique identifier or the `name` attribute of the Key Set that should be associated to the newly-created Key.
    create_key_set_request = kong_admin_client.CreateKeySetRequest() # CreateKeySetRequest |  (optional)

    try:
        # Update a Key-set
        api_response = api_instance.update_key_set(key_set_id_or_name, create_key_set_request=create_key_set_request)
        print("The response of KeySetsApi->update_key_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeySetsApi->update_key_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_set_id_or_name** | **str**| The unique identifier or the &#x60;name&#x60; attribute of the Key Set that should be associated to the newly-created Key. | 
 **create_key_set_request** | [**CreateKeySetRequest**](CreateKeySetRequest.md)|  | [optional] 

### Return type

[**ListKeySet200Response**](ListKeySet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key set object response body |  -  |
**400** | Invalid Key-set |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_key_set**
> ListKeySet200Response upsert_key_set(key_set_id_or_name, create_key_set_request=create_key_set_request)

Update a Key-set

Update a Key-set using ID or name.  > Note: This API is not available in DB-less mode.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_key_set_request import CreateKeySetRequest
from kong_admin_client.models.list_key_set200_response import ListKeySet200Response
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
    api_instance = kong_admin_client.KeySetsApi(api_client)
    key_set_id_or_name = '46CA83EE-671C-11ED-BFAB-2FE47512C77A' # str | The unique identifier or the `name` attribute of the Key Set that should be associated to the newly-created Key.
    create_key_set_request = kong_admin_client.CreateKeySetRequest() # CreateKeySetRequest |  (optional)

    try:
        # Update a Key-set
        api_response = api_instance.upsert_key_set(key_set_id_or_name, create_key_set_request=create_key_set_request)
        print("The response of KeySetsApi->upsert_key_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KeySetsApi->upsert_key_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_set_id_or_name** | **str**| The unique identifier or the &#x60;name&#x60; attribute of the Key Set that should be associated to the newly-created Key. | 
 **create_key_set_request** | [**CreateKeySetRequest**](CreateKeySetRequest.md)|  | [optional] 

### Return type

[**ListKeySet200Response**](ListKeySet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Key set object response body |  -  |
**400** | Invalid Key-set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

