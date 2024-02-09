# kong_admin_client.VaultsApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vault**](VaultsApi.md#create_vault) | **POST** /vaults | Create a new Vault
[**delete_vault**](VaultsApi.md#delete_vault) | **DELETE** /vaults/{vault_id_or_prefix} | Delete a Vault
[**get_vault**](VaultsApi.md#get_vault) | **GET** /vaults/{vault_id_or_prefix} | Fetch a Vault
[**list_vault**](VaultsApi.md#list_vault) | **GET** /vaults | List all Vaults
[**update_vault**](VaultsApi.md#update_vault) | **PATCH** /vaults/{vault_id_or_prefix} | Update a Vault
[**upsert_vault**](VaultsApi.md#upsert_vault) | **PUT** /vaults/{vault_id_or_prefix} | Upsert a Vault


# **create_vault**
> Vault create_vault(create_vault_request=create_vault_request)

Create a new Vault

Create a new Vault

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.create_vault_request import CreateVaultRequest
from kong_admin_client.models.vault import Vault
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
    api_instance = kong_admin_client.VaultsApi(api_client)
    create_vault_request = {"prefix":"env","name":"env","description":"This vault is used to retrieve redis database access credentials","config":{"prefix":"SSL_"},"tags":["database-credentials","data-plane"]} # CreateVaultRequest |  (optional)

    try:
        # Create a new Vault
        api_response = api_instance.create_vault(create_vault_request=create_vault_request)
        print("The response of VaultsApi->create_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->create_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vault_request** | [**CreateVaultRequest**](CreateVaultRequest.md)|  | [optional] 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created Vault |  -  |
**400** | Invalid Vault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vault**
> delete_vault(vault_id_or_prefix)

Delete a Vault

Delete a Vault

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
    api_instance = kong_admin_client.VaultsApi(api_client)
    vault_id_or_prefix = 'env' # str | The unique identifier or the prefix of the Vault to retrieve.

    try:
        # Delete a Vault
        api_instance.delete_vault(vault_id_or_prefix)
    except Exception as e:
        print("Exception when calling VaultsApi->delete_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id_or_prefix** | **str**| The unique identifier or the prefix of the Vault to retrieve. | 

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
**204** | Successfully deleted Vault or the resource didn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vault**
> Vault get_vault(vault_id_or_prefix)

Fetch a Vault

Get a Vault using ID or prefix.  Vault entities are used to configure different Vault connectors.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.vault import Vault
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
    api_instance = kong_admin_client.VaultsApi(api_client)
    vault_id_or_prefix = 'env' # str | The unique identifier or the prefix of the Vault to retrieve.

    try:
        # Fetch a Vault
        api_response = api_instance.get_vault(vault_id_or_prefix)
        print("The response of VaultsApi->get_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->get_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id_or_prefix** | **str**| The unique identifier or the prefix of the Vault to retrieve. | 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched Vault |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vault**
> ListVault200Response list_vault(size=size, offset=offset, tags=tags)

List all Vaults

List all Vaults

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.list_vault200_response import ListVault200Response
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
    api_instance = kong_admin_client.VaultsApi(api_client)
    size = 100 # int | Number of resources to be returned. (optional) (default to 100)
    offset = 'offset_example' # str | Offset from which to return the next set of resources. Use the value of the 'offset' field from the response of a list operation as input here to paginate through all the resources (optional)
    tags = 'tag1,tag2' # str | A list of tags to filter the list of resources on. Multiple tags can be concatenated using ','' to mean AND or using ''/'' to mean OR.' (optional)

    try:
        # List all Vaults
        api_response = api_instance.list_vault(size=size, offset=offset, tags=tags)
        print("The response of VaultsApi->list_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->list_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**| Number of resources to be returned. | [optional] [default to 100]
 **offset** | **str**| Offset from which to return the next set of resources. Use the value of the &#39;offset&#39; field from the response of a list operation as input here to paginate through all the resources | [optional] 
 **tags** | **str**| A list of tags to filter the list of resources on. Multiple tags can be concatenated using &#39;,&#39;&#39; to mean AND or using &#39;&#39;/&#39;&#39; to mean OR.&#39; | [optional] 

### Return type

[**ListVault200Response**](ListVault200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response listing Vaults |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vault**
> Vault update_vault(vault_id_or_prefix, create_vault_request=create_vault_request)

Update a Vault

Update a Vault

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.create_vault_request import CreateVaultRequest
from kong_admin_client.models.vault import Vault
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
    api_instance = kong_admin_client.VaultsApi(api_client)
    vault_id_or_prefix = 'env' # str | The unique identifier or the prefix of the Vault to retrieve.
    create_vault_request = {"prefix":"env","name":"env","description":"This vault is used to retrieve redis database access credentials","config":{"prefix":"SSL_"},"tags":["database-credentials","data-plane"]} # CreateVaultRequest |  (optional)

    try:
        # Update a Vault
        api_response = api_instance.update_vault(vault_id_or_prefix, create_vault_request=create_vault_request)
        print("The response of VaultsApi->update_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->update_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id_or_prefix** | **str**| The unique identifier or the prefix of the Vault to retrieve. | 
 **create_vault_request** | [**CreateVaultRequest**](CreateVaultRequest.md)|  | [optional] 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated Vault |  -  |
**400** | Invalid Vault |  -  |
**404** | Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_vault**
> Vault upsert_vault(vault_id_or_prefix, create_vault_request=create_vault_request)

Upsert a Vault

Create or Update Vault using ID or prefix.

### Example


```python
import time
import os
import kong_admin_client
from kong_admin_client.models.create_vault_request import CreateVaultRequest
from kong_admin_client.models.vault import Vault
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
    api_instance = kong_admin_client.VaultsApi(api_client)
    vault_id_or_prefix = 'env' # str | The unique identifier or the prefix of the Vault to retrieve.
    create_vault_request = {"prefix":"env","name":"env","description":"This vault is used to retrieve redis database access credentials","config":{"prefix":"SSL_"},"tags":["database-credentials","data-plane"]} # CreateVaultRequest |  (optional)

    try:
        # Upsert a Vault
        api_response = api_instance.upsert_vault(vault_id_or_prefix, create_vault_request=create_vault_request)
        print("The response of VaultsApi->upsert_vault:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VaultsApi->upsert_vault: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_id_or_prefix** | **str**| The unique identifier or the prefix of the Vault to retrieve. | 
 **create_vault_request** | [**CreateVaultRequest**](CreateVaultRequest.md)|  | [optional] 

### Return type

[**Vault**](Vault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully upserted Vault |  -  |
**400** | Invalid Vault |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

