# UpstreamHealthchecksPassive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | [**UpstreamHealthchecksPassiveHealthy**](UpstreamHealthchecksPassiveHealthy.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'http']
**unhealthy** | [**UpstreamHealthchecksPassiveUnhealthy**](UpstreamHealthchecksPassiveUnhealthy.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.upstream_healthchecks_passive import UpstreamHealthchecksPassive

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecksPassive from a JSON string
upstream_healthchecks_passive_instance = UpstreamHealthchecksPassive.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecksPassive.to_json()

# convert the object into a dict
upstream_healthchecks_passive_dict = upstream_healthchecks_passive_instance.to_dict()
# create an instance of UpstreamHealthchecksPassive from a dict
upstream_healthchecks_passive_form_dict = upstream_healthchecks_passive.from_dict(upstream_healthchecks_passive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


