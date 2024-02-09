# CreateUpstreamRequestHealthchecksActive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**https_verify_certificate** | **bool** |  | [optional] 
**healthy** | [**CreateUpstreamRequestHealthchecksActiveHealthy**](CreateUpstreamRequestHealthchecksActiveHealthy.md) |  | [optional] 
**unhealthy** | [**CreateUpstreamRequestHealthchecksActiveUnhealthy**](CreateUpstreamRequestHealthchecksActiveUnhealthy.md) |  | [optional] 
**type** | **str** | Whether to perform active health checks using HTTP or HTTPS, or just attempt a TCP connection. | [optional] [default to 'http']
**concurrency** | **int** | Number of targets to check concurrently in active health checks. | [optional] [default to 10]
**headers** | **object** | One or more lists of values indexed by header name to use in GET HTTP request to run as a probe on active health checks. Values must be pre-formatted. | [optional] 
**timeout** | **int** | Socket timeout for active health checks (in seconds). | [optional] [default to 1]
**http_path** | **str** | Path to use in GET HTTP request to run as a probe on active health checks. | [optional] [default to '/']
**https_sni** | **str** | The hostname to use as an SNI (Server Name Identification) when performing active health checks using HTTPS. This is particularly useful when Targets are configured using IPs, so that the target host&#39;s certificate can be verified with the proper SNI. | [optional] 

## Example

```python
from kong_admin_client.models.create_upstream_request_healthchecks_active import CreateUpstreamRequestHealthchecksActive

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestHealthchecksActive from a JSON string
create_upstream_request_healthchecks_active_instance = CreateUpstreamRequestHealthchecksActive.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestHealthchecksActive.to_json()

# convert the object into a dict
create_upstream_request_healthchecks_active_dict = create_upstream_request_healthchecks_active_instance.to_dict()
# create an instance of CreateUpstreamRequestHealthchecksActive from a dict
create_upstream_request_healthchecks_active_form_dict = create_upstream_request_healthchecks_active.from_dict(create_upstream_request_healthchecks_active_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


