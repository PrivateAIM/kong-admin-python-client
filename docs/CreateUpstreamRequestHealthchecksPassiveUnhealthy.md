# CreateUpstreamRequestHealthchecksPassiveUnhealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_statuses** | **List[int]** | An array of HTTP statuses which represent unhealthiness when produced by proxied traffic, as observed by passive health checks. With form-encoded, the notation is &#x60;http_statuses[]&#x3D;429&amp;http_statuses[]&#x3D;500&#x60;. With JSON, use an array. | [optional] [default to [429,500,503]]
**timeouts** | **int** | Number of timeouts in proxied traffic to consider a target unhealthy, as observed by passive health checks. | [optional] [default to 0]
**http_failures** | **int** | Number of HTTP failures in proxied traffic (as defined by &#x60;healthchecks.passive.unhealthy.http_statuses&#x60;) to consider a target unhealthy, as observed by passive health checks. | [optional] [default to 0]
**tcp_failures** | **int** | Number of TCP connection failures to consider a target unhealthy, as observed by passive health checks. | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks_passive_unhealthy import CreateUpstreamRequestHealthchecksPassiveUnhealthy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecksPassiveUnhealthy from a JSON string
create_upstream_request_healthchecks_passive_unhealthy_instance = CreateUpstreamRequestHealthchecksPassiveUnhealthy.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecksPassiveUnhealthy.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_passive_unhealthy_dict = create_upstream_request_healthchecks_passive_unhealthy_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecksPassiveUnhealthy from a dict
create_upstream_request_healthchecks_passive_unhealthy_form_dict = create_upstream_request_healthchecks_passive_unhealthy.from_dict(create_upstream_request_healthchecks_passive_unhealthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


