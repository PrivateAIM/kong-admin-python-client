# CreateKeyAuthForConsumerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer** | **str** | The id/username of the consumer that this Key will be associated with.  | [optional] 
**key** | **str** | The key to associate with the given consumer. If not specified, it will be auto-generated.  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Key for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.create_key_auth_for_consumer_request import CreateKeyAuthForConsumerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKeyAuthForConsumerRequest from a JSON string
create_key_auth_for_consumer_request_instance = CreateKeyAuthForConsumerRequest.from_json(json)
# print the JSON string representation of the object
print CreateKeyAuthForConsumerRequest.to_json()

# convert the object into a dict
create_key_auth_for_consumer_request_dict = create_key_auth_for_consumer_request_instance.to_dict()
# create an instance of CreateKeyAuthForConsumerRequest from a dict
create_key_auth_for_consumer_request_form_dict = create_key_auth_for_consumer_request.from_dict(create_key_auth_for_consumer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


