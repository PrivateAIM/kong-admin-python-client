# CreateUpstreamRequestHealthchecksPassiveHealthy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_statuses** | **List[int]** | An array of HTTP statuses which represent healthiness when produced by proxied traffic, as observed by passive health checks.  With form-encoded, the notation is &#x60;http_statuses[]&#x3D;200&amp;http_statuses[]&#x3D;201&#x60;. With JSON, use an array. | [optional] [default to [200,201,202,203,204,205,206,207,208,226,300,301,302,303,304,305,306,307,308]]
**successes** | **int** | Number of successes in proxied traffic (as defined by &#x60;healthchecks.passive.healthy.http_statuses&#x60;) to consider a target healthy, as observed by passive health checks. | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks_passive_healthy import CreateUpstreamRequestHealthchecksPassiveHealthy

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecksPassiveHealthy from a JSON string
create_upstream_request_healthchecks_passive_healthy_instance = CreateUpstreamRequestHealthchecksPassiveHealthy.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecksPassiveHealthy.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_passive_healthy_dict = create_upstream_request_healthchecks_passive_healthy_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecksPassiveHealthy from a dict
create_upstream_request_healthchecks_passive_healthy_form_dict = create_upstream_request_healthchecks_passive_healthy.from_dict(create_upstream_request_healthchecks_passive_healthy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


