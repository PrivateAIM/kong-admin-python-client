# CreatePluginForConsumerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Plugin that&#39;s going to be added. Currently, the Plugin must be installed in every Kong instance separately.  | [optional] 
**route** | **str** | If set, the plugin will only activate when receiving requests via the specified route. Leave unset for the plugin to activate regardless of the route being used. Default: &#x60;null&#x60;. With form-encoded, the notation is &#x60;route.id&#x3D;&lt;route id&gt; or route.name&#x3D;&lt;route name&gt;&#x60;. With JSON, use &#x60;\&quot;route\&quot;:{\&quot;id\&quot;:\&quot;&lt;route id&gt;\&quot;}&#x60; or &#x60;\&quot;route\&quot;:{\&quot;name\&quot;:\&quot;&lt;route name&gt;\&quot;}&#x60;.  | [optional] 
**service** | **str** | If set, the plugin will only activate when receiving requests via one of the routes belonging to the specified service.  | [optional] 
**consumer** | **str** | If set, the plugin will activate only for requests where the specified has been authenticated. (Note that some plugins can not be restricted to consumers this way.)  | [optional] 
**instance_name** | **str** | The Plugin instance name.  | [optional] 
**config** | [**ListPluginsForConsumer200ResponseConfig**](ListPluginsForConsumer200ResponseConfig.md) |  | [optional] 
**protocols** | **List[str]** | A list of the request protocols that will trigger this plugin. | [optional] 
**enabled** | **bool** | Whether the plugin is applied. Default: &#x60;true&#x60;.  | [optional] [default to True]
**tags** | **List[str]** | An optional set of strings associated with the Plugin for grouping and filtering.  | [optional] 
**ordering** | [**ListPluginsForConsumer200ResponseOrdering**](ListPluginsForConsumer200ResponseOrdering.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.create_plugin_for_consumer_request import CreatePluginForConsumerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePluginForConsumerRequest from a JSON string
create_plugin_for_consumer_request_instance = CreatePluginForConsumerRequest.from_json(json)
# print the JSON string representation of the object
print CreatePluginForConsumerRequest.to_json()

# convert the object into a dict
create_plugin_for_consumer_request_dict = create_plugin_for_consumer_request_instance.to_dict()
# create an instance of CreatePluginForConsumerRequest from a dict
create_plugin_for_consumer_request_form_dict = create_plugin_for_consumer_request.from_dict(create_plugin_for_consumer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


