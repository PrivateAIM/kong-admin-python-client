# GetTimers200ResponseStatsFlamegraph

String-encoded timer-related flamegraph data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **str** | The number of pending timers for the flamegraph | [optional] 
**running** | **str** | The number of running timers for the flamegraph | [optional] 
**elapsed_time** | **str** | The elapsed time for the flamegraph | [optional] 

## Example

```python
from kong_admin_client.models.get_timers200_response_stats_flamegraph import GetTimers200ResponseStatsFlamegraph

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimers200ResponseStatsFlamegraph from a JSON string
get_timers200_response_stats_flamegraph_instance = GetTimers200ResponseStatsFlamegraph.from_json(json)
# print the JSON string representation of the object
print GetTimers200ResponseStatsFlamegraph.to_json()

# convert the object into a dict
get_timers200_response_stats_flamegraph_dict = get_timers200_response_stats_flamegraph_instance.to_dict()
# create an instance of GetTimers200ResponseStatsFlamegraph from a dict
get_timers200_response_stats_flamegraph_form_dict = get_timers200_response_stats_flamegraph.from_dict(get_timers200_response_stats_flamegraph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


