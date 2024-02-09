# PluginRoute

If set, the plugin will only activate when receiving requests via the specified route. Leave unset for the plugin to activate regardless of the route being used.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.plugin_route import PluginRoute

# TODO update the JSON string below
json = "{}"
# create an instance of PluginRoute from a JSON string
plugin_route_instance = PluginRoute.from_json(json)
# print the JSON string representation of the object
print PluginRoute.to_json()

# convert the object into a dict
plugin_route_dict = plugin_route_instance.to_dict()
# create an instance of PluginRoute from a dict
plugin_route_form_dict = plugin_route.from_dict(plugin_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


