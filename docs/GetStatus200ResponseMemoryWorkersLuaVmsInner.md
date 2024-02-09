# GetStatus200ResponseMemoryWorkersLuaVmsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_allocated_gc** | **str** | HTTP submodule&#39;s Lua virtual machine&#39;s memory usage information, as reported by  | [optional] 
**pid** | **int** | worker&#39;s process identification number. | [optional] 

## Example

```python
from kong_admin_client.models.get_status200_response_memory_workers_lua_vms_inner import GetStatus200ResponseMemoryWorkersLuaVmsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200ResponseMemoryWorkersLuaVmsInner from a JSON string
get_status200_response_memory_workers_lua_vms_inner_instance = GetStatus200ResponseMemoryWorkersLuaVmsInner.from_json(json)
# print the JSON string representation of the object
print GetStatus200ResponseMemoryWorkersLuaVmsInner.to_json()

# convert the object into a dict
get_status200_response_memory_workers_lua_vms_inner_dict = get_status200_response_memory_workers_lua_vms_inner_instance.to_dict()
# create an instance of GetStatus200ResponseMemoryWorkersLuaVmsInner from a dict
get_status200_response_memory_workers_lua_vms_inner_form_dict = get_status200_response_memory_workers_lua_vms_inner.from_dict(get_status200_response_memory_workers_lua_vms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


