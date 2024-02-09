# CreateRouteRequestSourcesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_route_request_sources_inner import CreateRouteRequestSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRouteRequestSourcesInner from a JSON string
create_route_request_sources_inner_instance = CreateRouteRequestSourcesInner.from_json(json)
# print the JSON string representation of the object
print CreateRouteRequestSourcesInner.to_json()

# convert the object into a dict
create_route_request_sources_inner_dict = create_route_request_sources_inner_instance.to_dict()
# create an instance of CreateRouteRequestSourcesInner from a dict
create_route_request_sources_inner_form_dict = create_route_request_sources_inner.from_dict(create_route_request_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


