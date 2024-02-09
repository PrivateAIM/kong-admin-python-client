# UpstreamHealthchecksActiveUnhealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_failures** | **int** |  | [optional] [default to 0]
**http_statuses** | **List[int]** |  | [optional] [default to [429,404,500,501,502,503,504,505]]
**interval** | **float** |  | [optional] [default to 0]
**tcp_failures** | **int** |  | [optional] [default to 0]
**timeouts** | **int** |  | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.upstream_healthchecks_active_unhealthy import UpstreamHealthchecksActiveUnhealthy

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecksActiveUnhealthy from a JSON string
upstream_healthchecks_active_unhealthy_instance = UpstreamHealthchecksActiveUnhealthy.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecksActiveUnhealthy.to_json()

# convert the object into a dict
upstream_healthchecks_active_unhealthy_dict = upstream_healthchecks_active_unhealthy_instance.to_dict()
# create an instance of UpstreamHealthchecksActiveUnhealthy from a dict
upstream_healthchecks_active_unhealthy_form_dict = upstream_healthchecks_active_unhealthy.from_dict(upstream_healthchecks_active_unhealthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


