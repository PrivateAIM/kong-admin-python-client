# CreateRouteRequestHeaders

One or more lists of values indexed by header name that will cause this route to match if present in the request. The Host header cannot be used with this hosts should be specified using the `hosts` attribute. When headers contains only one value and that value starts with the special prefix` ~*`, the value is interpreted as a regular expression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_my_header** | **List[str]** |  | [optional] 
**x_another_header** | **List[str]** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_route_request_headers import CreateRouteRequestHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRouteRequestHeaders from a JSON string
create_route_request_headers_instance = CreateRouteRequestHeaders.from_json(json)
# print the JSON string representation of the object
print CreateRouteRequestHeaders.to_json()

# convert the object into a dict
create_route_request_headers_dict = create_route_request_headers_instance.to_dict()
# create an instance of CreateRouteRequestHeaders from a dict
create_route_request_headers_form_dict = create_route_request_headers.from_dict(create_route_request_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


