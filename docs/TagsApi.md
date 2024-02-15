# kong_admin_client.TagsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tags**](TagsApi.md#get_tags) | **GET** /tags | List all tags
[**get_tags_tags**](TagsApi.md#get_tags_tags) | **GET** /tags/{tags} | List entity by tag


# **get_tags**
> GetTags200Response get_tags()

List all tags

Returns a paginated list of all the tags in the system.  The list of entities will not be restricted to a single entity type: all the entities tagged with tags will be present on this list.  If an entity is tagged with more than one tag, the entity_id for that entity will appear more than once in the resulting list. Similarly, if several entities have been tagged with the same tag, the tag will appear in several items of this list.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_tags200_response import GetTags200Response
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
    api_instance = kong_admin_client.TagsApi(api_client)

    try:
        # List all tags
        api_response = api_instance.get_tags()
        print("The response of TagsApi->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTags200Response**](GetTags200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tags response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_tags**
> GetTags200Response get_tags_tags(tags)

List entity by tag

Returns the entities that have been tagged with the specified tag.  The list of entities will not be restricted to a single entity type: all the entities tagged with tags will be present on this list.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_tags200_response import GetTags200Response
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
    api_instance = kong_admin_client.TagsApi(api_client)
    tags = 'example' # str | Tags are strings associated to entities in Kong.

    try:
        # List entity by tag
        api_response = api_instance.get_tags_tags(tags)
        print("The response of TagsApi->get_tags_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tags_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | **str**| Tags are strings associated to entities in Kong. | 

### Return type

[**GetTags200Response**](GetTags200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tags response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

