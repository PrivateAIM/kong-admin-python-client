# CreateKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | [**CreateKeyRequestSet**](CreateKeyRequestSet.md) |  | [optional] 
**name** | **str** | The name to associate with the given keys.  | [optional] 
**kid** | **str** | A unique identifier for a key.  | 
**jwk** | **str** | A JSON Web Key represented as a string. | [optional] 
**pem** | [**CreateKeyRequestPem**](CreateKeyRequestPem.md) |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Key for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.create_key_request import CreateKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyRequest from a JSON string
create_key_request_instance = CreateKeyRequest.from_json(json)
# print the JSON string representation of the object
print CreateKeyRequest.to_json()

# convert the object into a dict
create_key_request_dict = create_key_request_instance.to_dict()
# create an instance of CreateKeyRequest from a dict
create_key_request_form_dict = create_key_request.from_dict(create_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


