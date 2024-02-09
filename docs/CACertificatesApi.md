# kong_admin_client.CACertificatesApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ca_certificate**](CACertificatesApi.md#create_ca_certificate) | **POST** /ca_certificates | Create a new CA certificate
[**delete_ca_certificate**](CACertificatesApi.md#delete_ca_certificate) | **DELETE** /ca_certificates/{ca_certificate_id} | Delete a CA Certificate
[**get_ca_certificate**](CACertificatesApi.md#get_ca_certificate) | **GET** /ca_certificates/{ca_certificate_id} | Fetch a CA certificate
[**list_ca_certificate**](CACertificatesApi.md#list_ca_certificate) | **GET** /ca_certificates | List all CA certificates
[**update_ca_certificate**](CACertificatesApi.md#update_ca_certificate) | **PATCH** /ca_certificates/{ca_certificate_id} | Update a CA Certificate
[**updatet_ca_certificate**](CACertificatesApi.md#updatet_ca_certificate) | **PUT** /ca_certificates/{ca_certificate_id} | Update a CA Certificate


# **create_ca_certificate**
> CACertificate create_ca_certificate(create_ca_certificate_request=create_ca_certificate_request)

Create a new CA certificate

Create a new Certificate Authority (CA) certificate. The request body must include the `cert` property, the certificate data in PEM format; it can also include `cert_digest`, a digest of the certificate in hex format for verifying the certificates integrity, and `tags`, an optional list of tags to categorize the certificate.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.ca_certificate import CACertificate
from kong_admin_client.models.create_ca_certificate_request import CreateCaCertificateRequest
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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    create_ca_certificate_request = kong_admin_client.CreateCaCertificateRequest() # CreateCaCertificateRequest | This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. (optional)

    try:
        # Create a new CA certificate
        api_response = api_instance.create_ca_certificate(create_ca_certificate_request=create_ca_certificate_request)
        print("The response of CACertificatesApi->create_ca_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CACertificatesApi->create_ca_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ca_certificate_request** | [**CreateCaCertificateRequest**](CreateCaCertificateRequest.md)| This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. | [optional] 

### Return type

[**CACertificate**](CACertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created certificate object. |  -  |
**400** | Invalid CA certificate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ca_certificate**
> delete_ca_certificate(ca_certificate_id)

Delete a CA Certificate

Delete the specified Certificate Authority (CA) certificate using the provided ca_certificate_id.

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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    ca_certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | ID of the related certificate

    try:
        # Delete a CA Certificate
        api_instance.delete_ca_certificate(ca_certificate_id)
    except Exception as e:
        print("Exception when calling CACertificatesApi->delete_ca_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_certificate_id** | **str**| ID of the related certificate | 

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
**204** | Successfully deleted CA Certificate or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ca_certificate**
> CACertificate get_ca_certificate(ca_certificate_id)

Fetch a CA certificate

Retrieve details about the specified Certificate Authority (CA) certificate using the provided path parameter `ca_certificate_id`.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.ca_certificate import CACertificate
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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    ca_certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | ID of the related certificate

    try:
        # Fetch a CA certificate
        api_response = api_instance.get_ca_certificate(ca_certificate_id)
        print("The response of CACertificatesApi->get_ca_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CACertificatesApi->get_ca_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_certificate_id** | **str**| ID of the related certificate | 

### Return type

[**CACertificate**](CACertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified CA certificate exists in the system, and the response includes details about the certificate. |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ca_certificate**
> CACertificate list_ca_certificate(size=size, offset=offset, tags=tags)

List all CA certificates

Retrieve a list of all available Certificate Authority (CA) certificates, including the certificate ID, creation date, and other details. You can use query parameters to filter the results by size or tags, for example `/ca-certificates?size=50&tags=enterprise`.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.ca_certificate import CACertificate
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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all CA certificates
        api_response = api_instance.list_ca_certificate(size=size, offset=offset, tags=tags)
        print("The response of CACertificatesApi->list_ca_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CACertificatesApi->list_ca_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**CACertificate**](CACertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing CA Certificates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ca_certificate**
> CACertificate update_ca_certificate(ca_certificate_id, create_ca_certificate_request=create_ca_certificate_request)

Update a CA Certificate

Update the specified Certificate Authority (CA) certificate using the provided ca_certificate_id. Use this endpoint to modify an existing CA certificate in the system. The request body should include the fields of the CA certificate that need to be updated.  > This API is not available in DB-less mode.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.ca_certificate import CACertificate
from kong_admin_client.models.create_ca_certificate_request import CreateCaCertificateRequest
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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    ca_certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | ID of the related certificate
    create_ca_certificate_request = kong_admin_client.CreateCaCertificateRequest() # CreateCaCertificateRequest | This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. (optional)

    try:
        # Update a CA Certificate
        api_response = api_instance.update_ca_certificate(ca_certificate_id, create_ca_certificate_request=create_ca_certificate_request)
        print("The response of CACertificatesApi->update_ca_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CACertificatesApi->update_ca_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_certificate_id** | **str**| ID of the related certificate | 
 **create_ca_certificate_request** | [**CreateCaCertificateRequest**](CreateCaCertificateRequest.md)| This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. | [optional] 

### Return type

[**CACertificate**](CACertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated CA Certificate |  -  |
**400** | Invalid CA Certificate |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatet_ca_certificate**
> CACertificate updatet_ca_certificate(ca_certificate_id, create_ca_certificate_request=create_ca_certificate_request)

Update a CA Certificate

Create or Update a CA Certificate using the provided path parameter `ca_certificate_id`.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.ca_certificate import CACertificate
from kong_admin_client.models.create_ca_certificate_request import CreateCaCertificateRequest
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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    ca_certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | ID of the related certificate
    create_ca_certificate_request = kong_admin_client.CreateCaCertificateRequest() # CreateCaCertificateRequest | This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. (optional)

    try:
        # Update a CA Certificate
        api_response = api_instance.updatet_ca_certificate(ca_certificate_id, create_ca_certificate_request=create_ca_certificate_request)
        print("The response of CACertificatesApi->updatet_ca_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CACertificatesApi->updatet_ca_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ca_certificate_id** | **str**| ID of the related certificate | 
 **create_ca_certificate_request** | [**CreateCaCertificateRequest**](CreateCaCertificateRequest.md)| This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. | [optional] 

### Return type

[**CACertificate**](CACertificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted CA Certificate |  -  |
**400** | Invalid CA Certificate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

