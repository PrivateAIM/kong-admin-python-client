# Plugin

A Plugin entity represents a plugin configuration that will be executed during the HTTP request/response lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | The configuration properties for the Plugin which can be found on the plugins documentation page in the [Kong Hub](https://docs.konghq.com/hub/). | [optional] 
**consumer** | [**PluginConsumer**](PluginConsumer.md) |  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**enabled** | **bool** | Whether the plugin is applied. | [optional] [default to True]
**id** | **str** |  | [optional] 
**instance_name** | **str** |  | [optional] 
**name** | **str** | The name of the Plugin thats going to be added. Currently, the Plugin must be installed in every Kong instance separately. | [optional] 
**ordering** | **object** |  | [optional] 
**protocols** | **List[str]** | A list of the request protocols that will trigger this plugin. The default value, as well as the possible values allowed on this field, may change depending on the plugin type. For example, plugins that only work in stream mode will only support &#x60;\&quot;tcp\&quot;&#x60; and &#x60;\&quot;tls\&quot;&#x60;. | [optional] [default to ["grpc","grpcs","http","https"]]
**route** | [**PluginRoute**](PluginRoute.md) |  | [optional] 
**service** | [**PluginService**](PluginService.md) |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Plugin for grouping and filtering. | [optional] 
**updated_at** | **int** | Unix epoch when the resource was last updated. | [optional] 

## Example

```python
from kong_admin_client.models.plugin import Plugin

# TODO update the JSON string below
json = "{}"
# create an instance of Plugin from a JSON string
plugin_instance = Plugin.from_json(json)
# print the JSON string representation of the object
print Plugin.to_json()

# convert the object into a dict
plugin_dict = plugin_instance.to_dict()
# create an instance of Plugin from a dict
plugin_form_dict = plugin.from_dict(plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


