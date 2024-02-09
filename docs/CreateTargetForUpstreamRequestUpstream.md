# CreateTargetForUpstreamRequestUpstream

The unique identifier or the name of the upstream for which to update the target. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier or the name of the upstream for which to update the target. | [optional] 

## Example

```python
from kong_admin_client.models.create_target_for_upstream_request_upstream import CreateTargetForUpstreamRequestUpstream

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetForUpstreamRequestUpstream from a JSON string
create_target_for_upstream_request_upstream_instance = CreateTargetForUpstreamRequestUpstream.from_json(json)
# print the JSON string representation of the object
print CreateTargetForUpstreamRequestUpstream.to_json()

# convert the object into a dict
create_target_for_upstream_request_upstream_dict = create_target_for_upstream_request_upstream_instance.to_dict()
# create an instance of CreateTargetForUpstreamRequestUpstream from a dict
create_target_for_upstream_request_upstream_form_dict = create_target_for_upstream_request_upstream.from_dict(create_target_for_upstream_request_upstream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


