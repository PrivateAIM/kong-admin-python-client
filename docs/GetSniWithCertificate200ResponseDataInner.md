# GetSniWithCertificate200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier or the name attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed. | [optional] 
**name** | **str** | The SNI name to associate with the given certificate.  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created.  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the SNIs for grouping and filtering.  | [optional] 
**certificate** | [**GetSniWithCertificate200ResponseDataInnerCertificate**](GetSniWithCertificate200ResponseDataInnerCertificate.md) |  | [optional] 

## Example

```python
from kong_admin_client.models.get_sni_with_certificate200_response_data_inner import GetSniWithCertificate200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSniWithCertificate200ResponseDataInner from a JSON string
get_sni_with_certificate200_response_data_inner_instance = GetSniWithCertificate200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetSniWithCertificate200ResponseDataInner.to_json()

# convert the object into a dict
get_sni_with_certificate200_response_data_inner_dict = get_sni_with_certificate200_response_data_inner_instance.to_dict()
# create an instance of GetSniWithCertificate200ResponseDataInner from a dict
get_sni_with_certificate200_response_data_inner_form_dict = get_sni_with_certificate200_response_data_inner.from_dict(get_sni_with_certificate200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


