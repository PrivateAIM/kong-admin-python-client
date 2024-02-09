# CreateKeySetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to associate with the given key-set.  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Key for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.create_key_set_request import CreateKeySetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeySetRequest from a JSON string
create_key_set_request_instance = CreateKeySetRequest.from_json(json)
# print the JSON string representation of the object
print CreateKeySetRequest.to_json()

# convert the object into a dict
create_key_set_request_dict = create_key_set_request_instance.to_dict()
# create an instance of CreateKeySetRequest from a dict
create_key_set_request_form_dict = create_key_set_request.from_dict(create_key_set_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


