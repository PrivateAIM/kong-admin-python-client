# UpstreamHealthchecksPassiveHealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_statuses** | **List[int]** |  | [optional] [default to [200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308]]
**successes** | **int** |  | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.upstream_healthchecks_passive_healthy import UpstreamHealthchecksPassiveHealthy

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecksPassiveHealthy from a JSON string
upstream_healthchecks_passive_healthy_instance = UpstreamHealthchecksPassiveHealthy.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecksPassiveHealthy.to_json()

# convert the object into a dict
upstream_healthchecks_passive_healthy_dict = upstream_healthchecks_passive_healthy_instance.to_dict()
# create an instance of UpstreamHealthchecksPassiveHealthy from a dict
upstream_healthchecks_passive_healthy_form_dict = upstream_healthchecks_passive_healthy.from_dict(upstream_healthchecks_passive_healthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


