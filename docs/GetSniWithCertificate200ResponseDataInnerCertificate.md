# GetSniWithCertificate200ResponseDataInnerCertificate

The id (a UUID) of the certificate with which to associate the SNI hostname. The Certificate must have a valid private key associated with it to be used by the SNI object. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier or the name attribute of the Certificate whose SNIs | [optional] 

## Example

```python
from kong_admin_client.models.get_sni_with_certificate200_response_data_inner_certificate import GetSniWithCertificate200ResponseDataInnerCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of GetSniWithCertificate200ResponseDataInnerCertificate from a JSON string
get_sni_with_certificate200_response_data_inner_certificate_instance = GetSniWithCertificate200ResponseDataInnerCertificate.from_json(json)
# print the JSON string representation of the object
print GetSniWithCertificate200ResponseDataInnerCertificate.to_json()

# convert the object into a dict
get_sni_with_certificate200_response_data_inner_certificate_dict = get_sni_with_certificate200_response_data_inner_certificate_instance.to_dict()
# create an instance of GetSniWithCertificate200ResponseDataInnerCertificate from a dict
get_sni_with_certificate200_response_data_inner_certificate_form_dict = get_sni_with_certificate200_response_data_inner_certificate.from_dict(get_sni_with_certificate200_response_data_inner_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


