# kong_admin_client.SNIsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sni**](SNIsApi.md#create_sni) | **POST** /snis | Create a new SNI
[**create_sni_for_certificate**](SNIsApi.md#create_sni_for_certificate) | **POST** /certificates/{certificate_name_or_id}/snis | Create a new SNI associated with a Certificate
[**delete_sni**](SNIsApi.md#delete_sni) | **DELETE** /snis/{sni_name_or_id} | Delete an SNI
[**delete_sni_for_certificate**](SNIsApi.md#delete_sni_for_certificate) | **DELETE** /certificates/{certificate_id}/snis/{sni_name_or_id} | Delete a an SNI associated with a Certificate
[**fetch_sni_with_certificate**](SNIsApi.md#fetch_sni_with_certificate) | **GET** /certificates/{certificate_id}/snis/{sni_name_or_id} | Fetch an SNI associated with a certificate
[**get_sni**](SNIsApi.md#get_sni) | **GET** /snis/{sni_name_or_id} | Fetch an SNI
[**get_sni_with_certificate**](SNIsApi.md#get_sni_with_certificate) | **GET** /certificates/{certificate_name_or_id}/snis | List SNIs associated with a certificate
[**list_sni**](SNIsApi.md#list_sni) | **GET** /snis | List all SNIs
[**update_sni**](SNIsApi.md#update_sni) | **PATCH** /snis/{sni_name_or_id} | Update an SNI
[**update_sni_for_certificate**](SNIsApi.md#update_sni_for_certificate) | **PATCH** /certificates/{certificate_id}/snis/{sni_name_or_id} | Update SNI associated to a certificate
[**upsert_sni**](SNIsApi.md#upsert_sni) | **PUT** /snis/{sni_name_or_id} | Update an SNI
[**upsert_sni_for_certificate**](SNIsApi.md#upsert_sni_for_certificate) | **PUT** /certificates/{certificate_id}/snis/{sni_name_or_id} | Upsert an SNI associated with a certificate


# **create_sni**
> GetSniWithCertificate200Response create_sni(create_sni_for_certificate_request=create_sni_for_certificate_request)

Create a new SNI

Create a new SNI

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    create_sni_for_certificate_request = kong_admin_client.CreateSniForCertificateRequest() # CreateSniForCertificateRequest | A JSON object containing the details of the new SNI, including the name, certificate, and tags. (optional)

    try:
        # Create a new SNI
        api_response = api_instance.create_sni(create_sni_for_certificate_request=create_sni_for_certificate_request)
        print("The response of SNIsApi->create_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->create_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sni_for_certificate_request** | [**CreateSniForCertificateRequest**](CreateSniForCertificateRequest.md)| A JSON object containing the details of the new SNI, including the name, certificate, and tags. | [optional] 

### Return type

[**GetSniWithCertificate200Response**](GetSniWithCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SNI response object |  -  |
**400** | Invalid SNI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sni_for_certificate**
> SNI create_sni_for_certificate(certificate_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)

Create a new SNI associated with a Certificate

Create a new SNI and associate it with a certificate in the system. Use this endpoint to add a new SNI to the system and link it to a specific certificate.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest
from kong_admin_client.models.sni import SNI
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    certificate_name_or_id = 'name' # str | The unique identifier or the `name` attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed.
    create_sni_for_certificate_request = kong_admin_client.CreateSniForCertificateRequest() # CreateSniForCertificateRequest | A JSON object containing the details of the new SNI, including the name, certificate, and tags. (optional)

    try:
        # Create a new SNI associated with a Certificate
        api_response = api_instance.create_sni_for_certificate(certificate_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)
        print("The response of SNIsApi->create_sni_for_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->create_sni_for_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_name_or_id** | **str**| The unique identifier or the &#x60;name&#x60; attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed. | 
 **create_sni_for_certificate_request** | [**CreateSniForCertificateRequest**](CreateSniForCertificateRequest.md)| A JSON object containing the details of the new SNI, including the name, certificate, and tags. | [optional] 

### Return type

[**SNI**](SNI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created SNI |  -  |
**400** | Invalid SNI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sni**
> delete_sni(sni_name_or_id)

Delete an SNI

Delete an SNI

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
    api_instance = kong_admin_client.SNIsApi(api_client)
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.

    try:
        # Delete an SNI
        api_instance.delete_sni(sni_name_or_id)
    except Exception as e:
        print("Exception when calling SNIsApi->delete_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 

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
**204** | Successfully deleted SNI or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sni_for_certificate**
> delete_sni_for_certificate(certificate_id, sni_name_or_id)

Delete a an SNI associated with a Certificate

Delete a an SNI associated with a Certificate using ID or name. 

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
    api_instance = kong_admin_client.SNIsApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.

    try:
        # Delete a an SNI associated with a Certificate
        api_instance.delete_sni_for_certificate(certificate_id, sni_name_or_id)
    except Exception as e:
        print("Exception when calling SNIsApi->delete_sni_for_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 

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
**204** | Successfully deleted SNI or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_sni_with_certificate**
> SNI fetch_sni_with_certificate(certificate_id, sni_name_or_id)

Fetch an SNI associated with a certificate

Get an SNI associated with a Certificate using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.sni import SNI
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.

    try:
        # Fetch an SNI associated with a certificate
        api_response = api_instance.fetch_sni_with_certificate(certificate_id, sni_name_or_id)
        print("The response of SNIsApi->fetch_sni_with_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->fetch_sni_with_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 

### Return type

[**SNI**](SNI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched SNI |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sni**
> GetSniWithCertificate200Response get_sni(sni_name_or_id)

Fetch an SNI

Get an SNI using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.

    try:
        # Fetch an SNI
        api_response = api_instance.get_sni(sni_name_or_id)
        print("The response of SNIsApi->get_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->get_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 

### Return type

[**GetSniWithCertificate200Response**](GetSniWithCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SNI response object |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sni_with_certificate**
> GetSniWithCertificate200Response get_sni_with_certificate(certificate_name_or_id, size=size, offset=offset, tags=tags)

List SNIs associated with a certificate

Retrieve a paginated list of all SNIs associated with a certificate. Use this endpoint to retrieve a list of SNIs that are linked to a specific certificate. You can use the optional query parameters to filter the results based on specific criteria. The response will include the list of SNIs and pagination information. See the response schema for details on the expected format of the response body.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    certificate_name_or_id = 'name' # str | The unique identifier or the `name` attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed.
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List SNIs associated with a certificate
        api_response = api_instance.get_sni_with_certificate(certificate_name_or_id, size=size, offset=offset, tags=tags)
        print("The response of SNIsApi->get_sni_with_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->get_sni_with_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_name_or_id** | **str**| The unique identifier or the &#x60;name&#x60; attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed. | 
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**GetSniWithCertificate200Response**](GetSniWithCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SNI response object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sni**
> GetSniWithCertificate200Response list_sni(size=size, offset=offset, tags=tags)

List all SNIs

List all SNIs

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all SNIs
        api_response = api_instance.list_sni(size=size, offset=offset, tags=tags)
        print("The response of SNIsApi->list_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->list_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**GetSniWithCertificate200Response**](GetSniWithCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SNI response object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sni**
> GetSniWithCertificate200Response update_sni(sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)

Update an SNI

Update an SNI

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.
    create_sni_for_certificate_request = kong_admin_client.CreateSniForCertificateRequest() # CreateSniForCertificateRequest | A JSON object containing the details of the new SNI, including the name, certificate, and tags. (optional)

    try:
        # Update an SNI
        api_response = api_instance.update_sni(sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)
        print("The response of SNIsApi->update_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->update_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 
 **create_sni_for_certificate_request** | [**CreateSniForCertificateRequest**](CreateSniForCertificateRequest.md)| A JSON object containing the details of the new SNI, including the name, certificate, and tags. | [optional] 

### Return type

[**GetSniWithCertificate200Response**](GetSniWithCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SNI response object |  -  |
**400** | Invalid SNI |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sni_for_certificate**
> SNI update_sni_for_certificate(certificate_id, sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)

Update SNI associated to a certificate

    Update an existing SNI associated with a certificate in the system using the SNI ID or name. The request body should include the fields of the SNI that need to be updated, such as the name, description, or other properties. If the request body contains valid data, the endpoint will update the SNI and return a success response. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest
from kong_admin_client.models.sni import SNI
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.
    create_sni_for_certificate_request = kong_admin_client.CreateSniForCertificateRequest() # CreateSniForCertificateRequest | A JSON object containing the details of the new SNI, including the name, certificate, and tags. (optional)

    try:
        # Update SNI associated to a certificate
        api_response = api_instance.update_sni_for_certificate(certificate_id, sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)
        print("The response of SNIsApi->update_sni_for_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->update_sni_for_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 
 **create_sni_for_certificate_request** | [**CreateSniForCertificateRequest**](CreateSniForCertificateRequest.md)| A JSON object containing the details of the new SNI, including the name, certificate, and tags. | [optional] 

### Return type

[**SNI**](SNI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated SNI |  -  |
**400** | Invalid SNI |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_sni**
> GetSniWithCertificate200Response upsert_sni(sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)

Update an SNI

Create or Update SNI using ID or name.

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.
    create_sni_for_certificate_request = kong_admin_client.CreateSniForCertificateRequest() # CreateSniForCertificateRequest | A JSON object containing the details of the new SNI, including the name, certificate, and tags. (optional)

    try:
        # Update an SNI
        api_response = api_instance.upsert_sni(sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)
        print("The response of SNIsApi->upsert_sni:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->upsert_sni: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 
 **create_sni_for_certificate_request** | [**CreateSniForCertificateRequest**](CreateSniForCertificateRequest.md)| A JSON object containing the details of the new SNI, including the name, certificate, and tags. | [optional] 

### Return type

[**GetSniWithCertificate200Response**](GetSniWithCertificate200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SNI response object |  -  |
**400** | Invalid SNI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_sni_for_certificate**
> SNI upsert_sni_for_certificate(certificate_id, sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)

Upsert an SNI associated with a certificate

Create or Update an SNI associated with a Certificate using ID or name.  Inserts (or replaces) the SNI under the requested resource with the definition specified in the body. The SNI will be identified via the name or id attribute.  When the name or id attribute has the structure of a UUID, the SNI being inserted/replaced will be identified by its id. Otherwise it will be identified by its name.  When creating a new SNI without specifying id (neither in the URL nor in the body), then it will be auto-generated. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest
from kong_admin_client.models.sni import SNI
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
    api_instance = kong_admin_client.SNIsApi(api_client)
    certificate_id = '7fca84d6-7d37-4a74-a7b0-93e576089a41' # str | The unique identifier of the Certificate to retrieve.
    sni_name_or_id = 'my-sni' # str | The unique identifier or the name of the SNI to retrieve.
    create_sni_for_certificate_request = kong_admin_client.CreateSniForCertificateRequest() # CreateSniForCertificateRequest | A JSON object containing the details of the new SNI, including the name, certificate, and tags. (optional)

    try:
        # Upsert an SNI associated with a certificate
        api_response = api_instance.upsert_sni_for_certificate(certificate_id, sni_name_or_id, create_sni_for_certificate_request=create_sni_for_certificate_request)
        print("The response of SNIsApi->upsert_sni_for_certificate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SNIsApi->upsert_sni_for_certificate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| The unique identifier of the Certificate to retrieve. | 
 **sni_name_or_id** | **str**| The unique identifier or the name of the SNI to retrieve. | 
 **create_sni_for_certificate_request** | [**CreateSniForCertificateRequest**](CreateSniForCertificateRequest.md)| A JSON object containing the details of the new SNI, including the name, certificate, and tags. | [optional] 

### Return type

[**SNI**](SNI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted SNI |  -  |
**400** | Invalid SNI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

