# Key

A Key object holds a representation of asymmetric keys in various formats. When Kong or a Kong plugin requires a specific public or private key to perform certain operations, it can use this entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**id** | **str** | The unique identifier or the prefix of the Vault to delete. | [optional] 
**jwk** | **str** | A JSON Web Key represented as a string. | [optional] 
**kid** | **str** | A unique identifier for a key. | [optional] 
**name** | **str** | The name to associate with the given keys. | [optional] 
**pem** | [**KeyPem**](KeyPem.md) |  | [optional] 
**set** | [**KeySet**](KeySet.md) |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Key for grouping and filtering. | [optional] 
**updated_at** | **int** | Unix epoch when the resource was last updated. | [optional] 

## Example

```python
from kong_admin_client.models.key import Key

# TODO update the JSON string below
json = "{}"
# create an instance of Key from a JSON string
key_instance = Key.from_json(json)
# print the JSON string representation of the object
print Key.to_json()

# convert the object into a dict
key_dict = key_instance.to_dict()
# create an instance of Key from a dict
key_form_dict = key.from_dict(key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


