# FilterChainRoute

The route to which this chain is applied. A filter chain must be applied to either a single route or a single service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.filter_chain_route import FilterChainRoute

# TODO update the JSON string below
json = "{}"
# create an instance of FilterChainRoute from a JSON string
filter_chain_route_instance = FilterChainRoute.from_json(json)
# print the JSON string representation of the object
print FilterChainRoute.to_json()

# convert the object into a dict
filter_chain_route_dict = filter_chain_route_instance.to_dict()
# create an instance of FilterChainRoute from a dict
filter_chain_route_form_dict = filter_chain_route.from_dict(filter_chain_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


