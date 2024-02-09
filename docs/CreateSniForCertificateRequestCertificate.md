# CreateSniForCertificateRequestCertificate

The id (a UUID) of the certificate with which to associate the SNI hostname. The Certificate must have a valid private key associated with it to be used by the SNI object. With form-encoded, the notation is `certificate.id=<certificate id>`. With JSON, use `\"certificate\":{\"id\":\"<certificate id>\"}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 91020192-062d-416f-a275-9addeeaffaf2 | [optional] 

## Example

```python
from kong_admin_client.models.create_sni_for_certificate_request_certificate import CreateSniForCertificateRequestCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSniForCertificateRequestCertificate from a JSON string
create_sni_for_certificate_request_certificate_instance = CreateSniForCertificateRequestCertificate.from_json(json)
# print the JSON string representation of the object
print CreateSniForCertificateRequestCertificate.to_json()

# convert the object into a dict
create_sni_for_certificate_request_certificate_dict = create_sni_for_certificate_request_certificate_instance.to_dict()
# create an instance of CreateSniForCertificateRequestCertificate from a dict
create_sni_for_certificate_request_certificate_form_dict = create_sni_for_certificate_request_certificate.from_dict(create_sni_for_certificate_request_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


