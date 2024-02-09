# CreateKeyRequestSet

The id (an UUID) of the key-set with which to associate the key .With form-encoded, the notation is `set.id=<set id>` or `set.name=<set name>`. With JSON, use `\"set\":{\"id\":\"<set id>\"}` or `\"set\":{\"name\":\"<set name>\"}.`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 46CA83EE-671C-11ED-BFAB-2FE47512C77A | [optional] 

## Example

```python
from kong_admin_client.models.create_key_request_set import CreateKeyRequestSet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyRequestSet from a JSON string
create_key_request_set_instance = CreateKeyRequestSet.from_json(json)
# print the JSON string representation of the object
print CreateKeyRequestSet.to_json()

# convert the object into a dict
create_key_request_set_dict = create_key_request_set_instance.to_dict()
# create an instance of CreateKeyRequestSet from a dict
create_key_request_set_form_dict = create_key_request_set.from_dict(create_key_request_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


