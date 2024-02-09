# CreateUpstreamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is a hostname, which must be equal to the &#x60;host&#x60; of a service. | 
**algorithm** | **str** | Which load balancing algorithm to use. Accepted values are: &#x60;\&quot;consistent-hashing\&quot;&#x60;, &#x60;\&quot;least-connections\&quot;&#x60;,&#x60; \&quot;round-robin\&quot;&#x60;. Default: &#x60;\&quot;round-robin\&quot;&#x60;.  | [optional] [default to 'round-robin']
**hash_on** | **str** | What to use as hashing input. Using none results in a weighted-round-robin scheme with no hashing | [optional] [default to 'none']
**hash_fallback** | **str** | What to use as hashing input if the primary hash_on does not return a hash (eg. header is missing, or no Consumer identified). Not available if hash_on is set to cookie. | [optional] [default to 'none']
**hash_on_header** | **str** | The header name to take the value from as hash input. Only required when &#x60;hash_on&#x60; is set to header. | [optional] 
**hash_fallback_header** | **str** | The header name to take the value from as hash input. Only required when hash_fallback is set to header. | [optional] [default to 'none']
**hash_on_cookie** | **str** | The cookie name to take the value from as hash input. Only required when &#x60;hash_on&#x60; or &#x60;hash_fallback&#x60; is set to &#x60;cookie&#x60;. If the specified cookie is not in the request, Kong will generate a value and set the cookie in the response. | [optional] 
**hash_on_cookie_path** | **str** | The cookie path to set in the response headers. Only required when &#x60;hash_on&#x60; or &#x60;hash_fallback&#x60; is set to &#x60;cookie&#x60;. | [optional] [default to '/']
**hash_on_query_arg** | **str** | The name of the query string argument to take the value from as hash input. Only required when &#x60;hash_on&#x60; is set to &#x60;query_arg&#x60;. | [optional] 
**hash_fallback_query_arg** | **str** | The name of the query string argument to take the value from as hash input. Only required when &#x60;hash_fallback&#x60; is set to &#x60;query_arg&#x60;. | [optional] 
**hash_on_uri_capture** | **str** | The name of the route URI capture to take the value from as hash input. Only required when &#x60;hash_on&#x60; is set to &#x60;uri_capture&#x60;. | [optional] 
**hash_fallback_uri_capture** | **str** | The name of the route URI capture to take the value from as hash input. Only required when &#x60;hash_fallback&#x60; is set to &#x60;uri_capture&#x60;. | [optional] 
**slots** | **int** | The number of slots in the load balancer algorithm. If the algorithm is set to &#x60;round-robin&#x60;, this setting determines the maximum number of slots. If the algorithm is set to &#x60;consistent-hashing&#x60;, this setting determines the actual number of slots in the algorithm. Accepts an integer in the range 10-65536. | [optional] [default to 10000]
**healthchecks** | [**CreateUpstreamRequestHealthchecks**](CreateUpstreamRequestHealthchecks.md) |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Upstream for grouping and filtering. | [optional] 
**host_header** | **str** | The hostname to be used as Host header when proxying requests through Kong. | [optional] 
**client_certificate** | [**CreateUpstreamRequestClientCertificate**](CreateUpstreamRequestClientCertificate.md) |  | [optional] 
**use_srv_name** | **bool** | If set, the balancer will use SRV hostname(if DNS Answer has SRV record) as the proxy upstream Host. | [optional] 

## Example

```python
from kong_admin_client.models.create_upstream_request import CreateUpstreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequest from a JSON string
create_upstream_request_instance = CreateUpstreamRequest.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequest.to_json()

# convert the object into a dict
create_upstream_request_dict = create_upstream_request_instance.to_dict()
# create an instance of CreateUpstreamRequest from a dict
create_upstream_request_form_dict = create_upstream_request.from_dict(create_upstream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


