# UpsertConsumer200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UpsertConsumer200ResponseDataInner]**](UpsertConsumer200ResponseDataInner.md) |  | [optional] 
**next** | **str** | Pagination information | [optional] 

## Example

```python
from kong_admin_client.models.upsert_consumer200_response import UpsertConsumer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertConsumer200Response from a JSON string
upsert_consumer200_response_instance = UpsertConsumer200Response.from_json(json)
# print the JSON string representation of the object
print UpsertConsumer200Response.to_json()

# convert the object into a dict
upsert_consumer200_response_dict = upsert_consumer200_response_instance.to_dict()
# create an instance of UpsertConsumer200Response from a dict
upsert_consumer200_response_form_dict = upsert_consumer200_response.from_dict(upsert_consumer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


