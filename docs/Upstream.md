# Upstream

The upstream object represents a virtual hostname and can be used to loadbalance incoming requests over multiple services (targets). So for example an upstream named `service.v1.xyz` for a service object whose `host` is `service.v1.xyz`. Requests for this service would be proxied to the targets defined within the upstream. An upstream also includes a health check, which is able to enable and disable targets based on their ability or inability to serve requests. The configuration for the health checker is stored in the upstream object, and applies to all of its targets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Which load balancing algorithm to use. | [optional] [default to 'round-robin']
**client_certificate** | [**UpstreamClientCertificate**](UpstreamClientCertificate.md) |  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**hash_fallback** | **str** | What to use as hashing input if the primary &#x60;hash_on&#x60; does not return a hash (eg. header is missing, or no Consumer identified). Not available if &#x60;hash_on&#x60; is set to &#x60;cookie&#x60;. | [optional] [default to 'none']
**hash_fallback_header** | **str** | The header name to take the value from as hash input. Only required when &#x60;hash_fallback&#x60; is set to &#x60;header&#x60;. | [optional] 
**hash_fallback_query_arg** | **str** | The name of the query string argument to take the value from as hash input. Only required when &#x60;hash_fallback&#x60; is set to &#x60;query_arg&#x60;. | [optional] 
**hash_fallback_uri_capture** | **str** | The name of the route URI capture to take the value from as hash input. Only required when &#x60;hash_fallback&#x60; is set to &#x60;uri_capture&#x60;. | [optional] 
**hash_on** | **str** | What to use as hashing input. Using &#x60;none&#x60; results in a weighted-round-robin scheme with no hashing. | [optional] [default to 'none']
**hash_on_cookie** | **str** | The cookie name to take the value from as hash input. Only required when &#x60;hash_on&#x60; or &#x60;hash_fallback&#x60; is set to &#x60;cookie&#x60;. If the specified cookie is not in the request, Kong will generate a value and set the cookie in the response. | [optional] 
**hash_on_cookie_path** | **str** | The cookie path to set in the response headers. Only required when &#x60;hash_on&#x60; or &#x60;hash_fallback&#x60; is set to &#x60;cookie&#x60;. | [optional] [default to '/']
**hash_on_header** | **str** | The header name to take the value from as hash input. Only required when &#x60;hash_on&#x60; is set to &#x60;header&#x60;. | [optional] 
**hash_on_query_arg** | **str** | The name of the query string argument to take the value from as hash input. Only required when &#x60;hash_on&#x60; is set to &#x60;query_arg&#x60;. | [optional] 
**hash_on_uri_capture** | **str** | The name of the route URI capture to take the value from as hash input. Only required when &#x60;hash_on&#x60; is set to &#x60;uri_capture&#x60;. | [optional] 
**healthchecks** | [**UpstreamHealthchecks**](UpstreamHealthchecks.md) |  | [optional] 
**host_header** | **str** | The hostname to be used as &#x60;Host&#x60; header when proxying requests through Kong. | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | This is a hostname, which must be equal to the &#x60;host&#x60; of a service. | [optional] 
**slots** | **int** | The number of slots in the load balancer algorithm. If &#x60;algorithm&#x60; is set to &#x60;round-robin&#x60;, this setting determines the maximum number of slots. If &#x60;algorithm&#x60; is set to &#x60;consistent-hashing&#x60;, this setting determines the actual number of slots in the algorithm. Accepts an integer in the range &#x60;10&#x60;-&#x60;65536&#x60;. | [optional] [default to 10000]
**tags** | **List[str]** | An optional set of strings associated with the Upstream for grouping and filtering. | [optional] 
**use_srv_name** | **bool** | If set, the balancer will use SRV hostname(if DNS Answer has SRV record) as the proxy upstream &#x60;Host&#x60;. | [optional] [default to False]

## Example

```python
from kong_admin_client.models.upstream import Upstream

# TODO update the JSON string below
json = "{}"
# create an instance of Upstream from a JSON string
upstream_instance = Upstream.from_json(json)
# print the JSON string representation of the object
print Upstream.to_json()

# convert the object into a dict
upstream_dict = upstream_instance.to_dict()
# create an instance of Upstream from a dict
upstream_form_dict = upstream.from_dict(upstream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


