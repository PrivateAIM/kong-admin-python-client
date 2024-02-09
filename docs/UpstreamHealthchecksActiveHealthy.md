# UpstreamHealthchecksActiveHealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_statuses** | **List[int]** |  | [optional] [default to [200,302]]
**interval** | **float** |  | [optional] [default to 0]
**successes** | **int** |  | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.upstream_healthchecks_active_healthy import UpstreamHealthchecksActiveHealthy

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecksActiveHealthy from a JSON string
upstream_healthchecks_active_healthy_instance = UpstreamHealthchecksActiveHealthy.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecksActiveHealthy.to_json()

# convert the object into a dict
upstream_healthchecks_active_healthy_dict = upstream_healthchecks_active_healthy_instance.to_dict()
# create an instance of UpstreamHealthchecksActiveHealthy from a dict
upstream_healthchecks_active_healthy_form_dict = upstream_healthchecks_active_healthy.from_dict(upstream_healthchecks_active_healthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


