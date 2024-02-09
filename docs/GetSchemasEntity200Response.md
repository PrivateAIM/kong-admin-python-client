# GetSchemasEntity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[GetSchemasEntity200ResponseFieldsInner]**](GetSchemasEntity200ResponseFieldsInner.md) | A value of a schema | [optional] 

## Example

```python
from kong_admin_client.models.get_schemas_entity200_response import GetSchemasEntity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSchemasEntity200Response from a JSON string
get_schemas_entity200_response_instance = GetSchemasEntity200Response.from_json(json)
# print the JSON string representation of the object
print GetSchemasEntity200Response.to_json()

# convert the object into a dict
get_schemas_entity200_response_dict = get_schemas_entity200_response_instance.to_dict()
# create an instance of GetSchemasEntity200Response from a dict
get_schemas_entity200_response_form_dict = get_schemas_entity200_response.from_dict(get_schemas_entity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


