# kong_admin_client.CertificatesApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate**](CertificatesApi.md#create_certificate) | **POST** /certificates | Create a new Certificate
[**delete_certificate**](CertificatesApi.md#delete_certificate) | **DELETE** /certificates/{certificate_id} | Delete a Certificate
[**get_certificate**](CertificatesApi.md#get_certificate) | **GET** /certificates/{certificate_id} | Fetch a Certificate
[**list_certificate**](CertificatesApi.md#list_certificate) | **GET** /certificates | List all certificates
[**update_certificate**](CertificatesApi.md#update_certificate) | **PATCH** /certificates/{certificate_id} | Update a Certificate
[**update_certificate_put**](CertificatesApi.md#update_certificate_put) | **PUT** /certificates/{certificate_id} | Update a Certificate


# **create_certificate**
> Certificate create_certificate(create_certificate_request=create_certificate_request)

Create a new Certificate

Create a new certificate with the provided details. Use this endpoint to add a new certificate to the system. The request body must include the certificate data and other details required for creating a new certificate.  > Note: This API is not available in DB-less mode.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.certificate import Certificate
from kong_admin_client.models.create_certificate_request import CreateCertificateRequest
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
    api_instance = kong_admin_client.CertificatesApi(api_client)
    create_certificate_request = kong_admin_client.CreateCertificateRequest() # CreateCertificateRequest |  (optional)

    try:
        # Create a new Certificate
        api_response = api_instance.create_certificate(create_certificate_request=create_certificate_request)
        print("The response of CertificatesApi->create_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->create_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_certificate_request** | [**CreateCertificateRequest**](CreateCertificateRequest.md)|  | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created Certificate |  -  |
**400** | Invalid Certificate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate**
> delete_certificate(certificate_id)

Delete a Certificate

Delete a Certificate  >Note: This API is not available in DB-less mode. 

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
    api_instance = kong_admin_client.CertificatesApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.

    try:
        # Delete a Certificate
        api_instance.delete_certificate(certificate_id)
    except Exception as e:
        print("Exception when calling CertificatesApi->delete_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 

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
**204** | Successfully deleted Certificate or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate**
> Certificate get_certificate(certificate_id)

Fetch a Certificate

Retrieve details about the specified certificate using the provided path parameter `certificate_id`.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.certificate import Certificate
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
    api_instance = kong_admin_client.CertificatesApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.

    try:
        # Fetch a Certificate
        api_response = api_instance.get_certificate(certificate_id)
        print("The response of CertificatesApi->get_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->get_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP 200 OK |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate**
> ListCertificate200Response list_certificate(size=size, offset=offset, tags=tags)

List all certificates

Retrieve a list of all available CA Certificate Authority (CA) certificates. You can use query parameters to filter the results by size or tags, for example `/certificates?size=50&tags=enterprise`.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.list_certificate200_response import ListCertificate200Response
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
    api_instance = kong_admin_client.CertificatesApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all certificates
        api_response = api_instance.list_certificate(size=size, offset=offset, tags=tags)
        print("The response of CertificatesApi->list_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->list_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListCertificate200Response**](ListCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Certificates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate**
> Certificate update_certificate(certificate_id, create_certificate_request=create_certificate_request)

Update a Certificate

Update a Certificate  Inserts (or replaces) the certificate under the requested `certificate_id`with the definition specified in the request body. When the `name` or `id` attribute has the structure of a UUID, the certificate being inserted/replaced will be identified by its `id`. Otherwise it will be identified by the `name`.  When creating a new Certificate without specifying `id` (neither in the path or the request body), then it will be auto-generated.  >Note: This API is not available in DB-less mode.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.certificate import Certificate
from kong_admin_client.models.create_certificate_request import CreateCertificateRequest
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
    api_instance = kong_admin_client.CertificatesApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.
    create_certificate_request = kong_admin_client.CreateCertificateRequest() # CreateCertificateRequest |  (optional)

    try:
        # Update a Certificate
        api_response = api_instance.update_certificate(certificate_id, create_certificate_request=create_certificate_request)
        print("The response of CertificatesApi->update_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->update_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 
 **create_certificate_request** | [**CreateCertificateRequest**](CreateCertificateRequest.md)|  | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Certificate |  -  |
**400** | Invalid Certificate |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_put**
> Certificate update_certificate_put(certificate_id, create_certificate_request=create_certificate_request)

Update a Certificate

Update details about the specified certificate using the provided path parameter `certificate_id`.  Inserts (or replaces) the certificate under the requested `certificate_id`with the definition specified in the request body. When the `name` or `id` attribute has the structure of a UUID, the certificate being inserted/replaced will be identified by its `id`. Otherwise it will be identified by the `name`.  When creating a new Certificate without specifying `id` (neither in the path or the request body), then it will be auto-generated.    > Note: This API is not available in DB-less mode. 

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.certificate import Certificate
from kong_admin_client.models.create_certificate_request import CreateCertificateRequest
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
    api_instance = kong_admin_client.CertificatesApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.
    create_certificate_request = kong_admin_client.CreateCertificateRequest() # CreateCertificateRequest |  (optional)

    try:
        # Update a Certificate
        api_response = api_instance.update_certificate_put(certificate_id, create_certificate_request=create_certificate_request)
        print("The response of CertificatesApi->update_certificate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->update_certificate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 
 **create_certificate_request** | [**CreateCertificateRequest**](CreateCertificateRequest.md)|  | [optional] 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Certificate |  -  |
**400** | Invalid Certificate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

