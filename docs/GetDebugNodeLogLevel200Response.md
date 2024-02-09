# GetDebugNodeLogLevel200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A message containing the current log level of the node. | [optional] 

## Example

```python
from kong_admin_client.models.get_debug_node_log_level200_response import GetDebugNodeLogLevel200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDebugNodeLogLevel200Response from a JSON string
get_debug_node_log_level200_response_instance = GetDebugNodeLogLevel200Response.from_json(json)
# print the JSON string representation of the object
print GetDebugNodeLogLevel200Response.to_json()

# convert the object into a dict
get_debug_node_log_level200_response_dict = get_debug_node_log_level200_response_instance.to_dict()
# create an instance of GetDebugNodeLogLevel200Response from a dict
get_debug_node_log_level200_response_form_dict = get_debug_node_log_level200_response.from_dict(get_debug_node_log_level200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


