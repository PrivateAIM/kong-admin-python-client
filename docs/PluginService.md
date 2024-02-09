# PluginService

If set, the plugin will only activate when receiving requests via one of the routes belonging to the specified service. Leave unset for the plugin to activate regardless of the service being matched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.plugin_service import PluginService

# TODO update the JSON string below
json = "{}"
# create an instance of PluginService from a JSON string
plugin_service_instance = PluginService.from_json(json)
# print the JSON string representation of the object
print PluginService.to_json()

# convert the object into a dict
plugin_service_dict = plugin_service_instance.to_dict()
# create an instance of PluginService from a dict
plugin_service_form_dict = plugin_service.from_dict(plugin_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


