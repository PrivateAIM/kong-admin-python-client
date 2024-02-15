# kong_admin_client.RoutesApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_route**](RoutesApi.md#create_route) | **POST** /routes | Create a new route
[**create_route_for_service**](RoutesApi.md#create_route_for_service) | **POST** /services/{service_id_or_name}/routes | Create a new route associated with a service
[**delete_route**](RoutesApi.md#delete_route) | **DELETE** /routes/{route_id_or_name} | Delete a route
[**delete_route_for_service**](RoutesApi.md#delete_route_for_service) | **DELETE** /services/{service_id_or_name}/routes/{route_id_or_name} | Delete a route associated with a service
[**fetch_route_for_service**](RoutesApi.md#fetch_route_for_service) | **GET** /services/{service_id_or_name}/routes/{route_id_or_name} | Fetch a route associated with a service
[**get_route**](RoutesApi.md#get_route) | **GET** /routes/{route_id_or_name} | Fetch a route
[**list_route**](RoutesApi.md#list_route) | **GET** /routes | List all routes
[**list_routes_for_service**](RoutesApi.md#list_routes_for_service) | **GET** /services/{service_id_or_name}/routes | List all routes associated with a service
[**update_route**](RoutesApi.md#update_route) | **PATCH** /routes/{route_id_or_name} | Update a route
[**update_route_for_service**](RoutesApi.md#update_route_for_service) | **PATCH** /services/{service_id_or_name}/routes/{route_id_or_name} | Update a route associated with a service
[**upsert_route**](RoutesApi.md#upsert_route) | **PUT** /routes/{route_id_or_name} | Update a route
[**upsert_route_for_service**](RoutesApi.md#upsert_route_for_service) | **PUT** /services/{service_id_or_name}/routes/{route_id_or_name} | Upsert a route associated with a service


# **create_route**
> Route create_route(create_route_request=create_route_request)

Create a new route

Create a new route

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_route_request import CreateRouteRequest
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    create_route_request = {"name":"my-route","protocols":["http","https"],"methods":["GET","POST"],"hosts":["example.com","foo.test"],"paths":["/foo","/bar"],"headers":{"x-my-header":["foo","bar"],"x-another-header":["bla"]},"https_redirect_status_code":426,"regex_priority":0,"strip_path":true,"path_handling":"v0","preserve_host":false,"request_buffering":true,"response_buffering":true,"tags":["user-level","low-priority"],"service":{"id":"af8330d3-dbdc-48bd-b1be-55b98608834b"}} # CreateRouteRequest | Route request body (optional)

    try:
        # Create a new route
        api_response = api_instance.create_route(create_route_request=create_route_request)
        print("The response of RoutesApi->create_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->create_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_route_request** | [**CreateRouteRequest**](CreateRouteRequest.md)| Route request body | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created route |  -  |
**400** | Invalid route |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_for_service**
> Route create_route_for_service(service_id_or_name, create_route_request=create_route_request)

Create a new route associated with a service

Create a new route associated with a service

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_route_request import CreateRouteRequest
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    create_route_request = {"name":"my-route","protocols":["http","https"],"methods":["GET","POST"],"hosts":["example.com","foo.test"],"paths":["/foo","/bar"],"headers":{"x-my-header":["foo","bar"],"x-another-header":["bla"]},"https_redirect_status_code":426,"regex_priority":0,"strip_path":true,"path_handling":"v0","preserve_host":false,"request_buffering":true,"response_buffering":true,"tags":["user-level","low-priority"],"service":{"id":"af8330d3-dbdc-48bd-b1be-55b98608834b"}} # CreateRouteRequest | Route request body (optional)

    try:
        # Create a new route associated with a service
        api_response = api_instance.create_route_for_service(service_id_or_name, create_route_request=create_route_request)
        print("The response of RoutesApi->create_route_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->create_route_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **create_route_request** | [**CreateRouteRequest**](CreateRouteRequest.md)| Route request body | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created route |  -  |
**400** | Invalid route |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route**
> delete_route(route_id_or_name)

Delete a route

Delete a route   > Note: This API is not available in DB-less mode.

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
    api_instance = kong_admin_client.RoutesApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.

    try:
        # Delete a route
        api_instance.delete_route(route_id_or_name)
    except Exception as e:
        print("Exception when calling RoutesApi->delete_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 

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
**204** | Successfully deleted route or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route_for_service**
> delete_route_for_service(service_id_or_name, route_id_or_name)

Delete a route associated with a service

Delete a route associated with a service using ID or name.

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
    api_instance = kong_admin_client.RoutesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.

    try:
        # Delete a route associated with a service
        api_instance.delete_route_for_service(service_id_or_name, route_id_or_name)
    except Exception as e:
        print("Exception when calling RoutesApi->delete_route_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 

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
**204** | Successfully deleted route or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_route_for_service**
> Route fetch_route_for_service(service_id_or_name, route_id_or_name)

Fetch a route associated with a service

Get a route associated with a service using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.

    try:
        # Fetch a route associated with a service
        api_response = api_instance.fetch_route_for_service(service_id_or_name, route_id_or_name)
        print("The response of RoutesApi->fetch_route_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->fetch_route_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched route |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route**
> Route get_route(route_id_or_name)

Fetch a route

Get a route using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.

    try:
        # Fetch a route
        api_response = api_instance.get_route(route_id_or_name)
        print("The response of RoutesApi->get_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->get_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched route |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_route**
> ListRoute200Response list_route(size=size, offset=offset, tags=tags)

List all routes

List all routes  route entities define rules to match client requests. Each route is associated with a service, and a service may have multiple routes associated to it. Every request matching a given route will be proxied to its associated service.  > Note: Path handling algorithms v1 was deprecated in Kong 3.0. From Kong 3.0, when router_flavor is set to expressions, route.path_handling will be unconfigurable and the path handling behavior will be \"v0\"; when router_flavor is set to traditional_compatible, the path handling behavior will be \"v0\" regardless of the value of route.path_handling. Only router_flavor = traditional will support path_handling \"v1\" behavior.

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_route200_response import ListRoute200Response
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all routes
        api_response = api_instance.list_route(size=size, offset=offset, tags=tags)
        print("The response of RoutesApi->list_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->list_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListRoute200Response**](ListRoute200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing routes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_routes_for_service**
> ListRoute200Response list_routes_for_service(service_id_or_name, size=size, offset=offset, tags=tags)

List all routes associated with a service

List all routes associated with a service

### Example


```python
import kong_admin_client
from kong_admin_client.models.list_route200_response import ListRoute200Response
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all routes associated with a service
        api_response = api_instance.list_routes_for_service(service_id_or_name, size=size, offset=offset, tags=tags)
        print("The response of RoutesApi->list_routes_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->list_routes_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListRoute200Response**](ListRoute200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing routes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_route**
> Route update_route(route_id_or_name, create_route_request=create_route_request)

Update a route

Update a route  > Note: This API is not available in DB-less mode.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_route_request import CreateRouteRequest
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    create_route_request = {"name":"my-route","protocols":["http","https"],"methods":["GET","POST"],"hosts":["example.com","foo.test"],"paths":["/foo","/bar"],"headers":{"x-my-header":["foo","bar"],"x-another-header":["bla"]},"https_redirect_status_code":426,"regex_priority":0,"strip_path":true,"path_handling":"v0","preserve_host":false,"request_buffering":true,"response_buffering":true,"tags":["user-level","low-priority"],"service":{"id":"af8330d3-dbdc-48bd-b1be-55b98608834b"}} # CreateRouteRequest | Route request body (optional)

    try:
        # Update a route
        api_response = api_instance.update_route(route_id_or_name, create_route_request=create_route_request)
        print("The response of RoutesApi->update_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->update_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **create_route_request** | [**CreateRouteRequest**](CreateRouteRequest.md)| Route request body | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated route |  -  |
**400** | Invalid route |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_route_for_service**
> Route update_route_for_service(service_id_or_name, route_id_or_name, create_route_request=create_route_request)

Update a route associated with a service

Update a route associated with a service using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_route_request import CreateRouteRequest
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    create_route_request = {"name":"my-route","protocols":["http","https"],"methods":["GET","POST"],"hosts":["example.com","foo.test"],"paths":["/foo","/bar"],"headers":{"x-my-header":["foo","bar"],"x-another-header":["bla"]},"https_redirect_status_code":426,"regex_priority":0,"strip_path":true,"path_handling":"v0","preserve_host":false,"request_buffering":true,"response_buffering":true,"tags":["user-level","low-priority"],"service":{"id":"af8330d3-dbdc-48bd-b1be-55b98608834b"}} # CreateRouteRequest | Route request body (optional)

    try:
        # Update a route associated with a service
        api_response = api_instance.update_route_for_service(service_id_or_name, route_id_or_name, create_route_request=create_route_request)
        print("The response of RoutesApi->update_route_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->update_route_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **create_route_request** | [**CreateRouteRequest**](CreateRouteRequest.md)| Route request body | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated route |  -  |
**400** | Invalid route |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_route**
> Route upsert_route(route_id_or_name, create_route_request=create_route_request)

Update a route

Create or Update route using ID or name.   > Note: This API is not available in DB-less mode.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_route_request import CreateRouteRequest
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    create_route_request = {"name":"my-route","protocols":["http","https"],"methods":["GET","POST"],"hosts":["example.com","foo.test"],"paths":["/foo","/bar"],"headers":{"x-my-header":["foo","bar"],"x-another-header":["bla"]},"https_redirect_status_code":426,"regex_priority":0,"strip_path":true,"path_handling":"v0","preserve_host":false,"request_buffering":true,"response_buffering":true,"tags":["user-level","low-priority"],"service":{"id":"af8330d3-dbdc-48bd-b1be-55b98608834b"}} # CreateRouteRequest | Route request body (optional)

    try:
        # Update a route
        api_response = api_instance.upsert_route(route_id_or_name, create_route_request=create_route_request)
        print("The response of RoutesApi->upsert_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->upsert_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **create_route_request** | [**CreateRouteRequest**](CreateRouteRequest.md)| Route request body | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted route |  -  |
**400** | Invalid route |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_route_for_service**
> Route upsert_route_for_service(service_id_or_name, route_id_or_name, create_route_request=create_route_request)

Upsert a route associated with a service

Create or Update a route associated with a service using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_route_request import CreateRouteRequest
from kong_admin_client.models.route import Route
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
    api_instance = kong_admin_client.RoutesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    route_id_or_name = 'my-route' # str | The unique identifier or the name of the route to retrieve.
    create_route_request = {"name":"my-route","protocols":["http","https"],"methods":["GET","POST"],"hosts":["example.com","foo.test"],"paths":["/foo","/bar"],"headers":{"x-my-header":["foo","bar"],"x-another-header":["bla"]},"https_redirect_status_code":426,"regex_priority":0,"strip_path":true,"path_handling":"v0","preserve_host":false,"request_buffering":true,"response_buffering":true,"tags":["user-level","low-priority"],"service":{"id":"af8330d3-dbdc-48bd-b1be-55b98608834b"}} # CreateRouteRequest | Route request body (optional)

    try:
        # Upsert a route associated with a service
        api_response = api_instance.upsert_route_for_service(service_id_or_name, route_id_or_name, create_route_request=create_route_request)
        print("The response of RoutesApi->upsert_route_for_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutesApi->upsert_route_for_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **route_id_or_name** | **str**| The unique identifier or the name of the route to retrieve. | 
 **create_route_request** | [**CreateRouteRequest**](CreateRouteRequest.md)| Route request body | [optional] 

### Return type

[**Route**](Route.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted route |  -  |
**400** | Invalid route |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

