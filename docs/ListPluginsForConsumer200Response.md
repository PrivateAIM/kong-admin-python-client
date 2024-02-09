# ListPluginsForConsumer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of the Plugin that&#39;s going to be added. Currently, the Plugin must be installed in every Kong instance separately.  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**route** | **str** | If set, the plugin will only activate when receiving requests via the specified route. Leave unset for the plugin to activate regardless of the route being used. With form-encoded, the notation is &#x60;route.id&#x3D;&lt;route id&gt; or route.name&#x3D;&lt;route name&gt;&#x60;. With JSON, use &#x60;\&quot;route\&quot;:{\&quot;id\&quot;:\&quot;&lt;route id&gt;\&quot;}&#x60; or &#x60;\&quot;route\&quot;:{\&quot;name\&quot;:\&quot;&lt;route name&gt;\&quot;}&#x60;. | [optional] 
**service** | **str** | If set, the plugin will only activate when receiving requests via one of the routes belonging to the specified service. | [optional] 
**consumer** | **str** | If set, the plugin will activate only for requests where the specified has been authenticated. (Note that some plugins can not be restricted to consumers this way.) | [optional] 
**instance_name** | **str** | The Plugin instance name.  | [optional] 
**config** | [**ListPluginsForConsumer200ResponseConfig**](ListPluginsForConsumer200ResponseConfig.md) |  | [optional] 
**protocols** | **List[str]** | A list of the request protocols that will trigger this plugin. | [optional] 
**enabled** | **bool** | Whether the plugin is applied. Default: &#x60;true&#x60;.  | [optional] [default to True]
**tags** | **List[str]** | An optional set of strings associated with the Plugin for grouping and filtering.  | [optional] 
**ordering** | [**ListPluginsForConsumer200ResponseOrdering**](ListPluginsForConsumer200ResponseOrdering.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.list_plugins_for_consumer200_response import ListPluginsForConsumer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPluginsForConsumer200Response from a JSON string
list_plugins_for_consumer200_response_instance = ListPluginsForConsumer200Response.from_json(json)
# print the JSON string representation of the object
print ListPluginsForConsumer200Response.to_json()

# convert the object into a dict
list_plugins_for_consumer200_response_dict = list_plugins_for_consumer200_response_instance.to_dict()
# create an instance of ListPluginsForConsumer200Response from a dict
list_plugins_for_consumer200_response_form_dict = list_plugins_for_consumer200_response.from_dict(list_plugins_for_consumer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


