# CreateUpstreamRequestHealthchecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passive** | [**CreateUpstreamRequestHealthchecksPassive**](CreateUpstreamRequestHealthchecksPassive.md) |  | [optional] 
**active** | [**CreateUpstreamRequestHealthchecksActive**](CreateUpstreamRequestHealthchecksActive.md) |  | [optional] 
**threshold** | **int** | The minimum percentage of the upstream&#39;s targets&#39; weight that must be available for the whole upstream to be considered healthy. | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks import CreateUpstreamRequestHealthchecks

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecks from a JSON string
create_upstream_request_healthchecks_instance = CreateUpstreamRequestHealthchecks.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecks.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_dict = create_upstream_request_healthchecks_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecks from a dict
create_upstream_request_healthchecks_form_dict = create_upstream_request_healthchecks.from_dict(create_upstream_request_healthchecks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


