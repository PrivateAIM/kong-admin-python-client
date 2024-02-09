# Route

Route entities define rules to match client requests. Every request matching a given route will be proxied to its associated service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**destinations** | [**List[RouteDestinationsInner]**](RouteDestinationsInner.md) | A list of IP destinations of incoming connections that match this route when using stream routing. Each entry is an object with fields \&quot;ip\&quot; (optionally in CIDR range notation) and/or \&quot;port\&quot;. | [optional] 
**headers** | **object** | One or more lists of values indexed by header name that will cause this route to match if present in the request. The &#x60;Host&#x60; header cannot be used with this hosts should be specified using the &#x60;hosts&#x60; attribute. When &#x60;headers&#x60; contains only one value and that value starts with the special prefix &#x60;~*&#x60;, the value is interpreted as a regular expression. | [optional] 
**hosts** | **List[str]** | A list of domain names that match this route. Note that the hosts value is case sensitive. | [optional] 
**https_redirect_status_code** | **int** | The status code Kong responds with when all properties of a route match except the protocol i.e. if the protocol of the request is &#x60;HTTP&#x60; instead of &#x60;HTTPS&#x60;. &#x60;Location&#x60; header is injected by Kong if the field is set to 301, 302, 307 or 308. This config applies only if the route is configured to only accept the &#x60;https&#x60; protocol. | [optional] [default to 426]
**id** | **str** |  | [optional] 
**methods** | **List[str]** | A list of HTTP methods that match this route. | [optional] 
**name** | **str** | The name of the route. Route names must be unique, and they are case sensitive. For example, there can be two different routes named \&quot;test\&quot; and \&quot;Test\&quot;. | [optional] 
**path_handling** | **str** | Controls how the service path, route path and requested path are combined when sending a request to the upstream. See above for a detailed description of each behavior. | [optional] [default to 'v0']
**paths** | **List[str]** | A list of paths that match this route. | [optional] 
**preserve_host** | **bool** | When matching a route via one of the &#x60;hosts&#x60; domain names, use the request &#x60;Host&#x60; header in the upstream request headers. If set to &#x60;false&#x60;, the upstream &#x60;Host&#x60; header will be that of the services &#x60;host&#x60;. | [optional] [default to False]
**protocols** | **List[str]** | An array of the protocols this route should allow. See the [route Object](#route-object) section for a list of accepted protocols. When set to only &#x60;\&quot;https\&quot;&#x60;, HTTP requests are answered with an upgrade error. When set to only &#x60;\&quot;http\&quot;&#x60;, HTTPS requests are answered with an error. | [optional] [default to ["http","https"]]
**regex_priority** | **int** | A number used to choose which route resolves a given request when several routes match it using regexes simultaneously. When two routes match the path and have the same &#x60;regex_priority&#x60;, the older one (lowest &#x60;created_at&#x60;) is used. Note that the priority for non-regex routes is different (longer non-regex routes are matched before shorter ones). | [optional] [default to 0]
**request_buffering** | **bool** | Whether to enable request body buffering or not. With HTTP 1.1, it may make sense to turn this off on services that receive data with chunked transfer encoding. | [optional] [default to True]
**response_buffering** | **bool** | Whether to enable response body buffering or not. With HTTP 1.1, it may make sense to turn this off on services that send data with chunked transfer encoding. | [optional] [default to True]
**service** | [**RouteService**](RouteService.md) |  | [optional] 
**snis** | **List[str]** | A list of SNIs that match this route when using stream routing. | [optional] 
**sources** | [**List[RouteDestinationsInner]**](RouteDestinationsInner.md) | A list of IP sources of incoming connections that match this route when using stream routing. Each entry is an object with fields \&quot;ip\&quot; (optionally in CIDR range notation) and/or \&quot;port\&quot;. | [optional] 
**strip_path** | **bool** | When matching a route via one of the &#x60;paths&#x60;, strip the matching prefix from the upstream request URL. | [optional] [default to True]
**tags** | **List[str]** | An optional set of strings associated with the route for grouping and filtering. | [optional] 
**updated_at** | **int** | Unix epoch when the resource was last updated. | [optional] 

## Example

```python
from kong_admin_client.models.route import Route

# TODO update the JSON string below
json = "{}"
# create an instance of Route from a JSON string
route_instance = Route.from_json(json)
# print the JSON string representation of the object
print Route.to_json()

# convert the object into a dict
route_dict = route_instance.to_dict()
# create an instance of Route from a dict
route_form_dict = route.from_dict(route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


