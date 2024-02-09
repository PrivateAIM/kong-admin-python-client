# UpsertConsumer200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier or the name attribute of the consumer. | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**username** | **str** | The unique username of the consumer. You must send either this field or&#x60; custom_i&#x60;d with the request. | [optional] 
**custom_id** | **str** | Field for storing an existing unique ID for the Consumer - useful for mapping Kong with users in your existing database. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Consumer for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.upsert_consumer200_response_data_inner import UpsertConsumer200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertConsumer200ResponseDataInner from a JSON string
upsert_consumer200_response_data_inner_instance = UpsertConsumer200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print UpsertConsumer200ResponseDataInner.to_json()

# convert the object into a dict
upsert_consumer200_response_data_inner_dict = upsert_consumer200_response_data_inner_instance.to_dict()
# create an instance of UpsertConsumer200ResponseDataInner from a dict
upsert_consumer200_response_data_inner_form_dict = upsert_consumer200_response_data_inner.from_dict(upsert_consumer200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


