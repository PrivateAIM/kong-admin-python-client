# UpstreamHealthchecksPassiveUnhealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_failures** | **int** |  | [optional] [default to 0]
**http_statuses** | **List[int]** |  | [optional] [default to [429,500,503]]
**tcp_failures** | **int** |  | [optional] [default to 0]
**timeouts** | **int** |  | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.upstream_healthchecks_passive_unhealthy import UpstreamHealthchecksPassiveUnhealthy

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecksPassiveUnhealthy from a JSON string
upstream_healthchecks_passive_unhealthy_instance = UpstreamHealthchecksPassiveUnhealthy.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecksPassiveUnhealthy.to_json()

# convert the object into a dict
upstream_healthchecks_passive_unhealthy_dict = upstream_healthchecks_passive_unhealthy_instance.to_dict()
# create an instance of UpstreamHealthchecksPassiveUnhealthy from a dict
upstream_healthchecks_passive_unhealthy_form_dict = upstream_healthchecks_passive_unhealthy.from_dict(upstream_healthchecks_passive_unhealthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


