# CreateTargetForUpstreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upstream** | [**CreateTargetForUpstreamRequestUpstream**](CreateTargetForUpstreamRequestUpstream.md) |  | [optional] 
**weight** | **int** | The weight this target gets within the upstream loadbalancer (&#x60;0&#x60;-&#x60;65535&#x60;). If the hostname resolves to an SRV record, the &#x60;weight&#x60; value will be overridden by the value from the DNS record. | [optional] [default to 100]
**tags** | **List[str]** | An optional set of strings associated with the Target for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.create_target_for_upstream_request import CreateTargetForUpstreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTargetForUpstreamRequest from a JSON string
create_target_for_upstream_request_instance = CreateTargetForUpstreamRequest.from_json(json)
# print the JSON string representation of the object
print CreateTargetForUpstreamRequest.to_json()

# convert the object into a dict
create_target_for_upstream_request_dict = create_target_for_upstream_request_instance.to_dict()
# create an instance of CreateTargetForUpstreamRequest from a dict
create_target_for_upstream_request_form_dict = create_target_for_upstream_request.from_dict(create_target_for_upstream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


