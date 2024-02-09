# kong_admin_client.ServicesApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServicesApi.md#create_service) | **POST** /services | Create a new service
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /services/{service_id_or_name} | Delete a service
[**get_service**](ServicesApi.md#get_service) | **GET** /services/{service_id_or_name} | Fetch a service
[**list_service**](ServicesApi.md#list_service) | **GET** /services | List all services
[**update_service**](ServicesApi.md#update_service) | **PATCH** /services/{service_id_or_name} | Update a service
[**upsert_service**](ServicesApi.md#upsert_service) | **PUT** /services/{service_id_or_name} | Upsert a service


# **create_service**
> Service create_service(create_service_request=create_service_request)

Create a new service

Create a new service

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.create_service_request import CreateServiceRequest
from kong_admin_client.models.service import Service
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
    api_instance = kong_admin_client.ServicesApi(api_client)
    create_service_request = {"name":"my-service","retries":5,"protocol":"http","host":"example.com","port":80,"path":"/some_api","connect_timeout":6000,"write_timeout":6000,"read_timeout":6000,"tags":["user-level"],"client_certificate":{"id":"4e3ad2e4-0bc4-4638-8e34-c84a417ba39b"},"tls_verify":true,"tls_verify_depth":null,"ca_certificates":["4e3ad2e4-0bc4-4638-8e34-c84a417ba39b"],"enabled":true} # CreateServiceRequest |  (optional)

    try:
        # Create a new service
        api_response = api_instance.create_service(create_service_request=create_service_request)
        print("The response of ServicesApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_service_request** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created service |  -  |
**400** | Invalid service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service**
> delete_service(service_id_or_name)

Delete a service

Delete a service

### Example


```python
import time
import os
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
    api_instance = kong_admin_client.ServicesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup

    try:
        # Delete a service
        api_instance.delete_service(service_id_or_name)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 

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
**204** | Successfully deleted service or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> Service get_service(service_id_or_name)

Fetch a service

Get a service using ID or name.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.service import Service
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
    api_instance = kong_admin_client.ServicesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup

    try:
        # Fetch a service
        api_response = api_instance.get_service(service_id_or_name)
        print("The response of ServicesApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched service |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service**
> ListService200Response list_service(size=size, offset=offset, tags=tags)

List all services

List all services

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.list_service200_response import ListService200Response
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
    api_instance = kong_admin_client.ServicesApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all services
        api_response = api_instance.list_service(size=size, offset=offset, tags=tags)
        print("The response of ServicesApi->list_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListService200Response**](ListService200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing services |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> Service update_service(service_id_or_name, create_service_request=create_service_request)

Update a service

Update a service

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.create_service_request import CreateServiceRequest
from kong_admin_client.models.service import Service
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
    api_instance = kong_admin_client.ServicesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    create_service_request = {"name":"my-service","retries":5,"protocol":"http","host":"example.com","port":80,"path":"/some_api","connect_timeout":6000,"write_timeout":6000,"read_timeout":6000,"tags":["user-level"],"client_certificate":{"id":"4e3ad2e4-0bc4-4638-8e34-c84a417ba39b"},"tls_verify":true,"tls_verify_depth":null,"ca_certificates":["4e3ad2e4-0bc4-4638-8e34-c84a417ba39b"],"enabled":true} # CreateServiceRequest |  (optional)

    try:
        # Update a service
        api_response = api_instance.update_service(service_id_or_name, create_service_request=create_service_request)
        print("The response of ServicesApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **create_service_request** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated service |  -  |
**400** | Invalid service |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_service**
> Service upsert_service(service_id_or_name, create_service_request=create_service_request)

Upsert a service

Create or Update service using ID or name.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.create_service_request import CreateServiceRequest
from kong_admin_client.models.service import Service
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
    api_instance = kong_admin_client.ServicesApi(api_client)
    service_id_or_name = 'test-service' # str | ID **or** name of the service to lookup
    create_service_request = {"name":"my-service","retries":5,"protocol":"http","host":"example.com","port":80,"path":"/some_api","connect_timeout":6000,"write_timeout":6000,"read_timeout":6000,"tags":["user-level"],"client_certificate":{"id":"4e3ad2e4-0bc4-4638-8e34-c84a417ba39b"},"tls_verify":true,"tls_verify_depth":null,"ca_certificates":["4e3ad2e4-0bc4-4638-8e34-c84a417ba39b"],"enabled":true} # CreateServiceRequest |  (optional)

    try:
        # Upsert a service
        api_response = api_instance.upsert_service(service_id_or_name, create_service_request=create_service_request)
        print("The response of ServicesApi->upsert_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->upsert_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id_or_name** | **str**| ID **or** name of the service to lookup | 
 **create_service_request** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted service |  -  |
**400** | Invalid service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

