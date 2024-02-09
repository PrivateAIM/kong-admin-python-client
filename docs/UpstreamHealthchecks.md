# UpstreamHealthchecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**UpstreamHealthchecksActive**](UpstreamHealthchecksActive.md) |  | [optional] 
**passive** | [**UpstreamHealthchecksPassive**](UpstreamHealthchecksPassive.md) |  | [optional] 
**threshold** | **float** |  | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.upstream_healthchecks import UpstreamHealthchecks

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecks from a JSON string
upstream_healthchecks_instance = UpstreamHealthchecks.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecks.to_json()

# convert the object into a dict
upstream_healthchecks_dict = upstream_healthchecks_instance.to_dict()
# create an instance of UpstreamHealthchecks from a dict
upstream_healthchecks_form_dict = upstream_healthchecks.from_dict(upstream_healthchecks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


