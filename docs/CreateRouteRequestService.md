# CreateRouteRequestService

The service this route is associated to. This is where the route proxies traffic to. With form-encoded, the notation is service.id=<service id> or service.name=<service name>. With JSON, use `\"service\":{\"id\":\"<service id>\"}` or `\"service\":{\"name\":\"<service name>\"}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_route_request_service import CreateRouteRequestService

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRouteRequestService from a JSON string
create_route_request_service_instance = CreateRouteRequestService.from_json(json)
# print the JSON string representation of the object
print CreateRouteRequestService.to_json()

# convert the object into a dict
create_route_request_service_dict = create_route_request_service_instance.to_dict()
# create an instance of CreateRouteRequestService from a dict
create_route_request_service_form_dict = create_route_request_service.from_dict(create_route_request_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


