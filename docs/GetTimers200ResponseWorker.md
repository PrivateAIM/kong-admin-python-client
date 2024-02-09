# GetTimers200ResponseWorker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ordinal number of the current Nginx worker processes (starting from number 0). | [optional] 
**count** | **int** | The total number of the Nginx worker processes. | [optional] 

## Example

```python
from kong_admin_client.models.get_timers200_response_worker import GetTimers200ResponseWorker

# TODO update the JSON string below
json = "{}"
# create an instance of GetTimers200ResponseWorker from a JSON string
get_timers200_response_worker_instance = GetTimers200ResponseWorker.from_json(json)
# print the JSON string representation of the object
print GetTimers200ResponseWorker.to_json()

# convert the object into a dict
get_timers200_response_worker_dict = get_timers200_response_worker_instance.to_dict()
# create an instance of GetTimers200ResponseWorker from a dict
get_timers200_response_worker_form_dict = get_timers200_response_worker.from_dict(get_timers200_response_worker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


