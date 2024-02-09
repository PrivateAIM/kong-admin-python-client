# GetSchemasEntity200ResponseFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**GetSchemasEntity200ResponseFieldsInnerId**](GetSchemasEntity200ResponseFieldsInnerId.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_schemas_entity200_response_fields_inner import GetSchemasEntity200ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSchemasEntity200ResponseFieldsInner from a JSON string
get_schemas_entity200_response_fields_inner_instance = GetSchemasEntity200ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print GetSchemasEntity200ResponseFieldsInner.to_json()

# convert the object into a dict
get_schemas_entity200_response_fields_inner_dict = get_schemas_entity200_response_fields_inner_instance.to_dict()
# create an instance of GetSchemasEntity200ResponseFieldsInner from a dict
get_schemas_entity200_response_fields_inner_form_dict = get_schemas_entity200_response_fields_inner.from_dict(get_schemas_entity200_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


