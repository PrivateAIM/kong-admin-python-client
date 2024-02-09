# GetTags200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetTags200ResponseDataInner]**](GetTags200ResponseDataInner.md) |  | [optional] 
**offset** | **str** | Pagination information | [optional] 
**next** | **str** | Pagination information | [optional] 

## Example

```python
from kong_admin_client.models.get_tags200_response import GetTags200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTags200Response from a JSON string
get_tags200_response_instance = GetTags200Response.from_json(json)
# print the JSON string representation of the object
print GetTags200Response.to_json()

# convert the object into a dict
get_tags200_response_dict = get_tags200_response_instance.to_dict()
# create an instance of GetTags200Response from a dict
get_tags200_response_form_dict = get_tags200_response.from_dict(get_tags200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


