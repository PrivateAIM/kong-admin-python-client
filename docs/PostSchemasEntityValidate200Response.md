# PostSchemasEntityValidate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A success message | [optional] 

## Example

```python
from kong_admin_client.models.post_schemas_entity_validate200_response import PostSchemasEntityValidate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostSchemasEntityValidate200Response from a JSON string
post_schemas_entity_validate200_response_instance = PostSchemasEntityValidate200Response.from_json(json)
# print the JSON string representation of the object
print PostSchemasEntityValidate200Response.to_json()

# convert the object into a dict
post_schemas_entity_validate200_response_dict = post_schemas_entity_validate200_response_instance.to_dict()
# create an instance of PostSchemasEntityValidate200Response from a dict
post_schemas_entity_validate200_response_form_dict = post_schemas_entity_validate200_response.from_dict(post_schemas_entity_validate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


