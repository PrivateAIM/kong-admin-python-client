# GetStatus200ResponseMemory

Metrics about the memory usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lua_shared_dicts** | [**GetStatus200ResponseMemoryLuaSharedDicts**](GetStatus200ResponseMemoryLuaSharedDicts.md) |  | [optional] 
**workers_lua_vms** | [**List[GetStatus200ResponseMemoryWorkersLuaVmsInner]**](GetStatus200ResponseMemoryWorkersLuaVmsInner.md) | An array with all workers of the Kong node, each entry contains a &#x60;http_allocated_gc&#x60; string and a &#x60;pid&#x60;. | [optional] 

## Example

```python
from kong_admin_client.models.get_status200_response_memory import GetStatus200ResponseMemory

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200ResponseMemory from a JSON string
get_status200_response_memory_instance = GetStatus200ResponseMemory.from_json(json)
# print the JSON string representation of the object
print GetStatus200ResponseMemory.to_json()

# convert the object into a dict
get_status200_response_memory_dict = get_status200_response_memory_instance.to_dict()
# create an instance of GetStatus200ResponseMemory from a dict
get_status200_response_memory_form_dict = get_status200_response_memory.from_dict(get_status200_response_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


