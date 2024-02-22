# ACLConsumer

The Consumer to which this ACL is associated. A Consumer can have many ACLs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.acl_consumer import ACLConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of ACLConsumer from a JSON string
acl_consumer_instance = ACLConsumer.from_json(json)
# print the JSON string representation of the object
print ACLConsumer.to_json()

# convert the object into a dict
acl_consumer_dict = acl_consumer_instance.to_dict()
# create an instance of ACLConsumer from a dict
acl_consumer_form_dict = acl_consumer.from_dict(acl_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


