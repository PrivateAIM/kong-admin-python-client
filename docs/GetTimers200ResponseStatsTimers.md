# GetTimers200ResponseStatsTimers

Timer statistics for the worker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**GetTimers200ResponseStatsTimersMeta**](GetTimers200ResponseStatsTimersMeta.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_timers200_response_stats_timers import GetTimers200ResponseStatsTimers

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimers200ResponseStatsTimers from a JSON string
get_timers200_response_stats_timers_instance = GetTimers200ResponseStatsTimers.from_json(json)
# print the JSON string representation of the object
print GetTimers200ResponseStatsTimers.to_json()

# convert the object into a dict
get_timers200_response_stats_timers_dict = get_timers200_response_stats_timers_instance.to_dict()
# create an instance of GetTimers200ResponseStatsTimers from a dict
get_timers200_response_stats_timers_form_dict = get_timers200_response_stats_timers.from_dict(get_timers200_response_stats_timers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


