# KeyAuth

A Key-auth entity represents a key used to authenticate consumers with the key-auth plugin. The key-auth plugin is used to protect API endpoints by requiring a secret key to be sent with the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer** | [**KeyAuthConsumer**](KeyAuthConsumer.md) |  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**id** | **str** |  | [optional] 
**key** | **str** | The key that will be used to authenticate the consumer. If this field is not specified, it will be auto-generated. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Key for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.key_auth import KeyAuth

# TODO update the JSON string below
json = "{}"
# create an instance of KeyAuth from a JSON string
key_auth_instance = KeyAuth.from_json(json)
# print the JSON string representation of the object
print KeyAuth.to_json()

# convert the object into a dict
key_auth_dict = key_auth_instance.to_dict()
# create an instance of KeyAuth from a dict
key_auth_form_dict = key_auth.from_dict(key_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


