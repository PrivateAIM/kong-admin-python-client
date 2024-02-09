# TargetUpstream

The unique identifier or the name of the upstream for which to update the target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.target_upstream import TargetUpstream

# TODO update the JSON string below
json = "{}"
# create an instance of TargetUpstream from a JSON string
target_upstream_instance = TargetUpstream.from_json(json)
# print the JSON string representation of the object
print TargetUpstream.to_json()

# convert the object into a dict
target_upstream_dict = target_upstream_instance.to_dict()
# create an instance of TargetUpstream from a dict
target_upstream_form_dict = target_upstream.from_dict(target_upstream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


