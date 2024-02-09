# CreateConsumerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The unique username of the Consumer. You must send either this field or custom_id with the request.  | 
**custom_id** | **str** | Field for storing an existing unique ID for the Consumer - useful for mapping Kong with users in your existing database. You must send either this field or username with the request.  | 
**tags** | **List[str]** | An optional set of strings associated with the Consumer for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.create_consumer_request import CreateConsumerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConsumerRequest from a JSON string
create_consumer_request_instance = CreateConsumerRequest.from_json(json)
# print the JSON string representation of the object
print CreateConsumerRequest.to_json()

# convert the object into a dict
create_consumer_request_dict = create_consumer_request_instance.to_dict()
# create an instance of CreateConsumerRequest from a dict
create_consumer_request_form_dict = create_consumer_request.from_dict(create_consumer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


