# GetTimers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stats** | [**GetTimers200ResponseStats**](GetTimers200ResponseStats.md) |  | [optional] 
**worker** | [**GetTimers200ResponseWorker**](GetTimers200ResponseWorker.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_timers200_response import GetTimers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimers200Response from a JSON string
get_timers200_response_instance = GetTimers200Response.from_json(json)
# print the JSON string representation of the object
print GetTimers200Response.to_json()

# convert the object into a dict
get_timers200_response_dict = get_timers200_response_instance.to_dict()
# create an instance of GetTimers200Response from a dict
get_timers200_response_form_dict = get_timers200_response.from_dict(get_timers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


