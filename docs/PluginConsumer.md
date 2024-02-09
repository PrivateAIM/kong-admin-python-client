# PluginConsumer

If set, the plugin will activate only for requests where the specified has been authenticated. (Note that some plugins can not be restricted to consumers this way.). Leave unset for the plugin to activate regardless of the authenticated Consumer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.plugin_consumer import PluginConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of PluginConsumer from a JSON string
plugin_consumer_instance = PluginConsumer.from_json(json)
# print the JSON string representation of the object
print PluginConsumer.to_json()

# convert the object into a dict
plugin_consumer_dict = plugin_consumer_instance.to_dict()
# create an instance of PluginConsumer from a dict
plugin_consumer_form_dict = plugin_consumer.from_dict(plugin_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


