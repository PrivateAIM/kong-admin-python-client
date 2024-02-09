# Consumer

The Consumer object represents a consumer - or a user - of a service. You can either rely on Kong as the primary datastore, or you can map the consumer list with your database to keep consistency between Kong and your existing primary datastore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**custom_id** | **str** | Field for storing an existing unique ID for the Consumer - useful for mapping Kong with users in your existing database. You must send either this field or &#x60;username&#x60; with the request. | [optional] 
**id** | **str** |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Consumer for grouping and filtering. | [optional] 
**username** | **str** | The unique username of the Consumer. You must send either this field or &#x60;custom_id&#x60; with the request. | [optional] 

## Example

```python
from kong_admin_client.models.consumer import Consumer

# TODO update the JSON string below
json = "{}"
# create an instance of Consumer from a JSON string
consumer_instance = Consumer.from_json(json)
# print the JSON string representation of the object
print Consumer.to_json()

# convert the object into a dict
consumer_dict = consumer_instance.to_dict()
# create an instance of Consumer from a dict
consumer_form_dict = consumer.from_dict(consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


