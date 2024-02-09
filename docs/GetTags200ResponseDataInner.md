# GetTags200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_name** | **str** | The name of the entity that corresponds to a tag | [optional] 
**entity_id** | **str** | The unique ID for the entity that is attached to the tag | [optional] 
**tag** | **str** | The tag | [optional] 

## Example

```python
from kong_admin_client.models.get_tags200_response_data_inner import GetTags200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTags200ResponseDataInner from a JSON string
get_tags200_response_data_inner_instance = GetTags200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetTags200ResponseDataInner.to_json()

# convert the object into a dict
get_tags200_response_data_inner_dict = get_tags200_response_data_inner_instance.to_dict()
# create an instance of GetTags200ResponseDataInner from a dict
get_tags200_response_data_inner_form_dict = get_tags200_response_data_inner.from_dict(get_tags200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


