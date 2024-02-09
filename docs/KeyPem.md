# KeyPem

A keypair in PEM format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.key_pem import KeyPem

# TODO update the JSON string below
json = "{}"
# create an instance of KeyPem from a JSON string
key_pem_instance = KeyPem.from_json(json)
# print the JSON string representation of the object
print KeyPem.to_json()

# convert the object into a dict
key_pem_dict = key_pem_instance.to_dict()
# create an instance of KeyPem from a dict
key_pem_form_dict = key_pem.from_dict(key_pem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


