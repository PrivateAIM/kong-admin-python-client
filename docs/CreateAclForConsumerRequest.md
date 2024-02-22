# CreateAclForConsumerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer** | **str** | The id/username of the consumer that this ACL will be associated with.  | [optional] 
**group** | **str** | The name of the group to associate with the given consumer.  | 
**tags** | **List[str]** | An optional set of strings associated with the ACL for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.create_acl_for_consumer_request import CreateAclForConsumerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAclForConsumerRequest from a JSON string
create_acl_for_consumer_request_instance = CreateAclForConsumerRequest.from_json(json)
# print the JSON string representation of the object
print CreateAclForConsumerRequest.to_json()

# convert the object into a dict
create_acl_for_consumer_request_dict = create_acl_for_consumer_request_instance.to_dict()
# create an instance of CreateAclForConsumerRequest from a dict
create_acl_for_consumer_request_form_dict = create_acl_for_consumer_request.from_dict(create_acl_for_consumer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


