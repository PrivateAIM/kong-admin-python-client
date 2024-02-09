# GetStatus200ResponseMemoryLuaSharedDicts

An array of information about dictionaries that are shared with all workers in a Kong node, where each array node contains how much memory is dedicated for the specific shared dictionary (capacity) and how much of said memory is in use (allocated_slabs).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kong_core_db_cache** | [**GetStatus200ResponseMemoryLuaSharedDictsKongCoreDbCache**](GetStatus200ResponseMemoryLuaSharedDictsKongCoreDbCache.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_status200_response_memory_lua_shared_dicts import GetStatus200ResponseMemoryLuaSharedDicts

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200ResponseMemoryLuaSharedDicts from a JSON string
get_status200_response_memory_lua_shared_dicts_instance = GetStatus200ResponseMemoryLuaSharedDicts.from_json(json)
# print the JSON string representation of the object
print GetStatus200ResponseMemoryLuaSharedDicts.to_json()

# convert the object into a dict
get_status200_response_memory_lua_shared_dicts_dict = get_status200_response_memory_lua_shared_dicts_instance.to_dict()
# create an instance of GetStatus200ResponseMemoryLuaSharedDicts from a dict
get_status200_response_memory_lua_shared_dicts_form_dict = get_status200_response_memory_lua_shared_dicts.from_dict(get_status200_response_memory_lua_shared_dicts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


