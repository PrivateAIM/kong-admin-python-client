# CreateKeyRequestPem

A keypair in PEM format. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **str** |  | [optional] 
**public_key** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_key_request_pem import CreateKeyRequestPem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyRequestPem from a JSON string
create_key_request_pem_instance = CreateKeyRequestPem.from_json(json)
# print the JSON string representation of the object
print CreateKeyRequestPem.to_json()

# convert the object into a dict
create_key_request_pem_dict = create_key_request_pem_instance.to_dict()
# create an instance of CreateKeyRequestPem from a dict
create_key_request_pem_form_dict = create_key_request_pem.from_dict(create_key_request_pem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


