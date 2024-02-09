# GetStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | [**GetStatus200ResponseMemory**](GetStatus200ResponseMemory.md) |  | [optional] 
**database** | [**GetStatus200ResponseDatabase**](GetStatus200ResponseDatabase.md) |  | [optional] 
**server** | [**GetStatus200ResponseServer**](GetStatus200ResponseServer.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_status200_response import GetStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200Response from a JSON string
get_status200_response_instance = GetStatus200Response.from_json(json)
# print the JSON string representation of the object
print GetStatus200Response.to_json()

# convert the object into a dict
get_status200_response_dict = get_status200_response_instance.to_dict()
# create an instance of GetStatus200Response from a dict
get_status200_response_form_dict = get_status200_response.from_dict(get_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


