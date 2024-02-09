# UpstreamHealthchecksActive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** |  | [optional] [default to 10]
**headers** | **object** |  | [optional] 
**healthy** | [**UpstreamHealthchecksActiveHealthy**](UpstreamHealthchecksActiveHealthy.md) |  | [optional] 
**http_path** | **str** |  | [optional] [default to '/']
**https_sni** | **str** |  | [optional] 
**https_verify_certificate** | **bool** |  | [optional] [default to True]
**timeout** | **float** |  | [optional] [default to 1]
**type** | **str** |  | [optional] [default to 'http']
**unhealthy** | [**UpstreamHealthchecksActiveUnhealthy**](UpstreamHealthchecksActiveUnhealthy.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.upstream_healthchecks_active import UpstreamHealthchecksActive

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamHealthchecksActive from a JSON string
upstream_healthchecks_active_instance = UpstreamHealthchecksActive.from_json(json)
# print the JSON string representation of the object
print UpstreamHealthchecksActive.to_json()

# convert the object into a dict
upstream_healthchecks_active_dict = upstream_healthchecks_active_instance.to_dict()
# create an instance of UpstreamHealthchecksActive from a dict
upstream_healthchecks_active_form_dict = upstream_healthchecks_active.from_dict(upstream_healthchecks_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


