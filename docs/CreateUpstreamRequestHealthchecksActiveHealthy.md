# CreateUpstreamRequestHealthchecksActiveHealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_statuses** | **List[int]** | An array of HTTP statuses to consider a success, indicating healthiness, when returned by a probe in active health checks. With form-encoded, the notation is &#x60;http_statuses[]&#x3D;200&amp;http_statuses[]&#x3D;302&#x60;. With JSON, use an array. | [optional] [default to [200,302]]
**successes** | **int** | Number of successes in active probes (as defined by &#x60;healthchecks.active.healthy.http_statuses&#x60;) to consider a target healthy. | [optional] [default to 0]
**interval** | **int** | Interval between active health checks for healthy targets (in seconds). A value of zero indicates that active probes for healthy targets should not be performed. | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks_active_healthy import CreateUpstreamRequestHealthchecksActiveHealthy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecksActiveHealthy from a JSON string
create_upstream_request_healthchecks_active_healthy_instance = CreateUpstreamRequestHealthchecksActiveHealthy.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecksActiveHealthy.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_active_healthy_dict = create_upstream_request_healthchecks_active_healthy_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecksActiveHealthy from a dict
create_upstream_request_healthchecks_active_healthy_form_dict = create_upstream_request_healthchecks_active_healthy.from_dict(create_upstream_request_healthchecks_active_healthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


