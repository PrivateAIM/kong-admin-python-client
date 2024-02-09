# CreateRouteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the route. Route names must be unique, and they are case sensitive. For example, there can be two different routes named \&quot;test\&quot; and \&quot;Test\&quot;.  | [optional] 
**protocols** | **List[str]** | An array of the protocols this route should allow | 
**methods** | **List[str]** | A list of HTTP methods that match this route.  | [optional] 
**hosts** | **List[str]** | A list of domain names that match this route. Note that the hosts value is case sensitive. With form-encoded, the notation is &#x60;hosts[]&#x3D;example.com&amp;hosts[]&#x3D;foo.test&#x60;. With JSON, use an Array. | [optional] 
**paths** | **List[str]** | A list of paths that match this route. With form-encoded, the notation is &#x60;paths[]&#x3D;/foo&amp;paths[]&#x3D;/bar&#x60;. With JSON, use an array. The path can be a regular expression, or a plain text pattern. | [optional] 
**headers** | [**CreateRouteRequestHeaders**](CreateRouteRequestHeaders.md) |  | [optional] 
**https_redirect_status_code** | **int** | The status code Kong responds with when all properties of a route match except the protocol i.e. if the protocol of the request is &#x60;HTTP&#x60; instead of &#x60;HTTPS&#x60; Location header is injected by Kong if the field is set to &#x60;301&#x60;, &#x60;302&#x60;, &#x60;307&#x60; or &#x60;308&#x60;. Note: This config applies only if the route is configured to only accept the https protocol. Accepted values are: &#x60;426&#x60;, &#x60;301&#x60;, &#x60;302&#x60;, &#x60;307&#x60;, &#x60;308&#x60;. Default: &#x60;426&#x60;. | [default to 426]
**regex_priority** | **int** | A number used to choose which route resolves a given request when several routes match it using regexes simultaneously. When two routes match the path and have the same regex_priority, the older one (lowest &#x60;created_at&#x60;) is used. Note that the priority for non-regex routes is different (longer non-regex routes are matched before shorter ones). | [optional] [default to 0]
**strip_path** | **bool** | When matching a route via one of the paths, strip the matching prefix from the upstream request URL. | [optional] [default to True]
**path_handling** | **str** | Controls how the service path, route path and requested path are combined when sending a request to the upstream. Accepted values are \&quot;&#x60;v0&#x60;\&quot;, \&quot;&#x60;v1&#x60;\&quot;. | [optional] 
**preserve_host** | **bool** | When matching a route via one of the &#x60;hosts&#x60; domain names, use the request &#x60;host&#x60; header in the upstream request headers. If set to &#x60;false&#x60;, the upstream Host header will be that of the service&#39;s host.  | [default to True]
**request_buffering** | **bool** | Whether to enable request body buffering or not. With HTTP 1.1, it may make sense to turn this off on services that receive data with chunked transfer encoding. Default: true.  | [default to True]
**response_buffering** | **bool** | Whether to enable response body buffering or not. With HTTP 1.1, it may make sense to turn this off on services that send data with chunked transfer encoding. Default: &#x60;true&#x60;.  | [default to True]
**snis** | **List[str]** | A list of SNIs that match this route when using stream routing.  | [optional] 
**sources** | [**List[CreateRouteRequestSourcesInner]**](CreateRouteRequestSourcesInner.md) | A list of IP sources of incoming connections that match this route when using stream routing. Each entry is an object with fields \&quot;ip\&quot; (optionally in CIDR range notation) and/or \&quot;port\&quot;.  | [optional] 
**destinations** | [**List[CreateRouteRequestDestinationsInner]**](CreateRouteRequestDestinationsInner.md) | A list of IP destinations of incoming connections that match this route when using stream routing. Each entry is an object with fields \&quot;ip\&quot; (optionally in CIDR range notation) and/or \&quot;port\&quot;.  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the route for grouping and filtering.  | [optional] 
**service** | [**CreateRouteRequestService**](CreateRouteRequestService.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.create_route_request import CreateRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRouteRequest from a JSON string
create_route_request_instance = CreateRouteRequest.from_json(json)
# print the JSON string representation of the object
print CreateRouteRequest.to_json()

# convert the object into a dict
create_route_request_dict = create_route_request_instance.to_dict()
# create an instance of CreateRouteRequest from a dict
create_route_request_form_dict = create_route_request.from_dict(create_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


