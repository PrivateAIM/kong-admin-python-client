# CreateUpstreamRequestHealthchecksPassive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether to perform passive health checks interpreting HTTP/HTTPS statuses, or just check for TCP connection success. In passive checks, http and https options are equivalent. Accepted values are &#x60;tcp&#x60;, &#x60;http&#x60;, &#x60;https&#x60;, &#x60;grpc&#x60;, &#x60;grpcs&#x60;. | [optional] [default to 'http']
**healthy** | [**CreateUpstreamRequestHealthchecksPassiveHealthy**](CreateUpstreamRequestHealthchecksPassiveHealthy.md) |  | [optional] 
**unhealthy** | [**CreateUpstreamRequestHealthchecksPassiveUnhealthy**](CreateUpstreamRequestHealthchecksPassiveUnhealthy.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks_passive import CreateUpstreamRequestHealthchecksPassive

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecksPassive from a JSON string
create_upstream_request_healthchecks_passive_instance = CreateUpstreamRequestHealthchecksPassive.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecksPassive.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_passive_dict = create_upstream_request_healthchecks_passive_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecksPassive from a dict
create_upstream_request_healthchecks_passive_form_dict = create_upstream_request_healthchecks_passive.from_dict(create_upstream_request_healthchecks_passive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


