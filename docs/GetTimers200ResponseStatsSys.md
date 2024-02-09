# GetTimers200ResponseStatsSys

List of the number of different type of timers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of timers (running + pending + waiting) | [optional] [default to 7]
**waiting** | **int** | The number of unexpired timers | [optional] [default to 7]
**runs** | **int** | The total number of runs for the timers | [optional] [default to 7]
**pending** | **int** | The number of pending timers | [optional] [default to 0]
**running** | **int** | The number of running timers | [optional] [default to 0]

## Example

```python
from kong_admin_client.models.get_timers200_response_stats_sys import GetTimers200ResponseStatsSys

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimers200ResponseStatsSys from a JSON string
get_timers200_response_stats_sys_instance = GetTimers200ResponseStatsSys.from_json(json)
# print the JSON string representation of the object
print GetTimers200ResponseStatsSys.to_json()

# convert the object into a dict
get_timers200_response_stats_sys_dict = get_timers200_response_stats_sys_instance.to_dict()
# create an instance of GetTimers200ResponseStatsSys from a dict
get_timers200_response_stats_sys_form_dict = get_timers200_response_stats_sys.from_dict(get_timers200_response_stats_sys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


