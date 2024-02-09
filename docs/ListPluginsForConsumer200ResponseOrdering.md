# ListPluginsForConsumer200ResponseOrdering

Describes a dependency to another plugin to determine plugin ordering during the access phase. - `before`: The plugin will be executed before a specified plugin or list of plugins. - `after`: The plugin will be executed after a specified plugin or list of plugins. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **List[str]** |  | [optional] 

## Example

```python
from kong_admin_client.models.list_plugins_for_consumer200_response_ordering import ListPluginsForConsumer200ResponseOrdering

# TODO update the JSON string below
json = "{}"
# create an instance of ListPluginsForConsumer200ResponseOrdering from a JSON string
list_plugins_for_consumer200_response_ordering_instance = ListPluginsForConsumer200ResponseOrdering.from_json(json)
# print the JSON string representation of the object
print ListPluginsForConsumer200ResponseOrdering.to_json()

# convert the object into a dict
list_plugins_for_consumer200_response_ordering_dict = list_plugins_for_consumer200_response_ordering_instance.to_dict()
# create an instance of ListPluginsForConsumer200ResponseOrdering from a dict
list_plugins_for_consumer200_response_ordering_form_dict = list_plugins_for_consumer200_response_ordering.from_dict(list_plugins_for_consumer200_response_ordering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


