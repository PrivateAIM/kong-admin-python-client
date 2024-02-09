# GetSniWithCertificate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetSniWithCertificate200ResponseDataInner]**](GetSniWithCertificate200ResponseDataInner.md) | Array of SNIs | [optional] 
**next** | **str** | Offset is used to paginate through the API. Provide this value to the next list operation to fetch the next page | [optional] 

## Example

```python
from kong_admin_client.models.get_sni_with_certificate200_response import GetSniWithCertificate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSniWithCertificate200Response from a JSON string
get_sni_with_certificate200_response_instance = GetSniWithCertificate200Response.from_json(json)
# print the JSON string representation of the object
print GetSniWithCertificate200Response.to_json()

# convert the object into a dict
get_sni_with_certificate200_response_dict = get_sni_with_certificate200_response_instance.to_dict()
# create an instance of GetSniWithCertificate200Response from a dict
get_sni_with_certificate200_response_form_dict = get_sni_with_certificate200_response.from_dict(get_sni_with_certificate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


