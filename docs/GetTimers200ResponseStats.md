# GetTimers200ResponseStats

Statistics about the worker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sys** | [**GetTimers200ResponseStatsSys**](GetTimers200ResponseStatsSys.md) |  | [optional] 
**flamegraph** | [**GetTimers200ResponseStatsFlamegraph**](GetTimers200ResponseStatsFlamegraph.md) |  | [optional] 
**timers** | [**GetTimers200ResponseStatsTimers**](GetTimers200ResponseStatsTimers.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_timers200_response_stats import GetTimers200ResponseStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimers200ResponseStats from a JSON string
get_timers200_response_stats_instance = GetTimers200ResponseStats.from_json(json)
# print the JSON string representation of the object
print GetTimers200ResponseStats.to_json()

# convert the object into a dict
get_timers200_response_stats_dict = get_timers200_response_stats_instance.to_dict()
# create an instance of GetTimers200ResponseStats from a dict
get_timers200_response_stats_form_dict = get_timers200_response_stats.from_dict(get_timers200_response_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


