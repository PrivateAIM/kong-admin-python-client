# ListVault200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Vault]**](Vault.md) |  | [optional] 
**offset** | **str** | Offset is used to paginate through the API. Provide this value to the next list operation to fetch the next page | [optional] 

## Example

```python
from kong_admin_client.models.list_vault200_response import ListVault200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListVault200Response from a JSON string
list_vault200_response_instance = ListVault200Response.from_json(json)
# print the JSON string representation of the object
print ListVault200Response.to_json()

# convert the object into a dict
list_vault200_response_dict = list_vault200_response_instance.to_dict()
# create an instance of ListVault200Response from a dict
list_vault200_response_form_dict = list_vault200_response.from_dict(list_vault200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


