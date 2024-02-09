# ListPluginsForConsumer200ResponseConfig

The configuration properties for the Plugin

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hour** | **int** |  | [optional] 
**minute** | **int** |  | [optional] 

## Example

```python
from kong_admin_client.models.list_plugins_for_consumer200_response_config import ListPluginsForConsumer200ResponseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ListPluginsForConsumer200ResponseConfig from a JSON string
list_plugins_for_consumer200_response_config_instance = ListPluginsForConsumer200ResponseConfig.from_json(json)
# print the JSON string representation of the object
print ListPluginsForConsumer200ResponseConfig.to_json()

# convert the object into a dict
list_plugins_for_consumer200_response_config_dict = list_plugins_for_consumer200_response_config_instance.to_dict()
# create an instance of ListPluginsForConsumer200ResponseConfig from a dict
list_plugins_for_consumer200_response_config_form_dict = list_plugins_for_consumer200_response_config.from_dict(list_plugins_for_consumer200_response_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


