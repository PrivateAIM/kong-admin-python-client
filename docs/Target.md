# Target

A target is an ip address/hostname with a port that identifies an instance of a backend service. Every upstream can have many targets, and the targets can be dynamically added, modified, or deleted. Changes take effect on the fly. To disable a target, post a new one with `weight=0`; alternatively, use the `DELETE` convenience method to accomplish the same. The current target object definition is the one with the latest `created_at`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **float** | Unix epoch when the resource was created. | [optional] 
**id** | **str** | The unique identifier or the name of the upstream for which to update the target. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Target for grouping and filtering. | [optional] 
**target** | **str** | The target address (ip or hostname) and port. If the hostname resolves to an SRV record, the &#x60;port&#x60; value will be overridden by the value from the DNS record. | [optional] 
**upstream** | [**TargetUpstream**](TargetUpstream.md) |  | [optional] 
**weight** | **int** | The weight this target gets within the upstream loadbalancer (&#x60;0&#x60;-&#x60;65535&#x60;). If the hostname resolves to an SRV record, the &#x60;weight&#x60; value will be overridden by the value from the DNS record. | [optional] [default to 100]

## Example

```python
from kong_admin_client.models.target import Target

# TODO update the JSON string below
json = "{}"
# create an instance of Target from a JSON string
target_instance = Target.from_json(json)
# print the JSON string representation of the object
print Target.to_json()

# convert the object into a dict
target_dict = target_instance.to_dict()
# create an instance of Target from a dict
target_form_dict = target.from_dict(target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


