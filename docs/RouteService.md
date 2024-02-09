# RouteService

The service this route is associated to. This is where the route proxies traffic to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.route_service import RouteService

# TODO update the JSON string below
json = "{}"
# create an instance of RouteService from a JSON string
route_service_instance = RouteService.from_json(json)
# print the JSON string representation of the object
print RouteService.to_json()

# convert the object into a dict
route_service_dict = route_service_instance.to_dict()
# create an instance of RouteService from a dict
route_service_form_dict = route_service.from_dict(route_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


