# ACL

ACL entities are used to control access to a resource. An ACL can be applied to a Consumer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumer** | [**ACLConsumer**](ACLConsumer.md) |  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**id** | **str** |  | [optional] 
**group** | **str** | The group that this ACL represents. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the ACL for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.acl import ACL

# TODO update the JSON string below
json = "{}"
# create an instance of ACL from a JSON string
acl_instance = ACL.from_json(json)
# print the JSON string representation of the object
print ACL.to_json()

# convert the object into a dict
acl_dict = acl_instance.to_dict()
# create an instance of ACL from a dict
acl_form_dict = acl.from_dict(acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


