# CreateSniForCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The SNI name to associate with the given certificate. | 
**tags** | **List[str]** | An optional set of strings associated with the SNIs for grouping and filtering.  | [optional] 
**certificate** | [**CreateSniForCertificateRequestCertificate**](CreateSniForCertificateRequestCertificate.md) |  | 

## Example

```python
from kong_admin_client.models.create_sni_for_certificate_request import CreateSniForCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSniForCertificateRequest from a JSON string
create_sni_for_certificate_request_instance = CreateSniForCertificateRequest.from_json(json)
# print the JSON string representation of the object
print CreateSniForCertificateRequest.to_json()

# convert the object into a dict
create_sni_for_certificate_request_dict = create_sni_for_certificate_request_instance.to_dict()
# create an instance of CreateSniForCertificateRequest from a dict
create_sni_for_certificate_request_form_dict = create_sni_for_certificate_request.from_dict(create_sni_for_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


