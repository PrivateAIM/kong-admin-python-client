# CreateUpstreamRequestHealthchecksActiveUnhealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_failures** | **int** | Number of HTTP failures in active probes (as defined by &#x60;healthchecks.active.unhealthy.http_statuses&#x60;) to consider a target unhealthy. | [optional] [default to 0]
**http_statuses** | **List[int]** | An array of HTTP statuses to consider a failure, indicating unhealthiness, when returned by a probe in active health checks. With form-encoded, the notation is &#x60;http_statuses[]&#x3D;429&amp;http_statuses[]&#x3D;404&#x60;. With JSON, use an array. | [optional] [default to [429,404,500,501,502,503,504,505]]
**timeouts** | **int** | Number of timeouts in active probes to consider a target unhealthy. | [optional] [default to 0]
**tcp_failures** | **int** | Number of TCP failures in active probes to consider a target unhealthy. | [optional] [default to 0]
**interval** | **int** | Interval between active health checks for unhealthy targets (in seconds). A value of zero indicates that active probes for unhealthy targets should not be performed. | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks_active_unhealthy import CreateUpstreamRequestHealthchecksActiveUnhealthy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecksActiveUnhealthy from a JSON string
create_upstream_request_healthchecks_active_unhealthy_instance = CreateUpstreamRequestHealthchecksActiveUnhealthy.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecksActiveUnhealthy.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_active_unhealthy_dict = create_upstream_request_healthchecks_active_unhealthy_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecksActiveUnhealthy from a dict
create_upstream_request_healthchecks_active_unhealthy_form_dict = create_upstream_request_healthchecks_active_unhealthy.from_dict(create_upstream_request_healthchecks_active_unhealthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


