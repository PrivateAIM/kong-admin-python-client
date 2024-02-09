# KeySet

The id (an UUID) of the key-set with which to associate the key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.key_set import KeySet

# TODO update the JSON string below
json = "{}"
# create an instance of KeySet from a JSON string
key_set_instance = KeySet.from_json(json)
# print the JSON string representation of the object
print KeySet.to_json()

# convert the object into a dict
key_set_dict = key_set_instance.to_dict()
# create an instance of KeySet from a dict
key_set_form_dict = key_set.from_dict(key_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


