# Certificate

A certificate object represents a public certificate. These fields are _referenceable_, and can be stored as [secrets](http://docs.konqhq.com/gateway/latest/plan-and-deploy/security/secrets-management/getting-started) in a vault. References must follow a [specific format](/gateway/latest/plan-and-deploy/security/secrets-management/reference-format).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | PEM-encoded public certificate chain of the SSL key This field is referenceable and can be stored in a vault. References must follow a [specific format](/gateway/latest/plan-and-deploy/security/secrets-management/reference-format). | [optional] 
**cert_alt** | **str** | PEM-encoded public certificate chain of the alternate SSL key pair. This should only be set if you have both RSA and ECDSA types of certificate available and would like Kong to prefer serving using ECDSA certs. | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**id** | **str** | The UUID representation of the certificate object. | [optional] 
**key** | **str** | PEM-encoded private key of the SSL key pair. This field is _referenceable_, which means it can be securely stored as a [secret](/gateway/latest/plan-and-deploy/security/secrets-management/getting-started) in a vault. References must follow a [specific format](/gateway/latest/plan-and-deploy/security/secrets-management/reference-format). | [optional] 
**key_alt** | **str** | PEM-encoded private key of the alternate SSL key pair. This should only be set if you have both RSA and ECDSA types of certificate available and would like Kong to prefer serving using ECDSA certs when client advertises support for it. This field is _referenceable_, which means it can be securely stored as a [secret](/gateway/latest/plan-and-deploy/security/secrets-management/getting-started) in a vault. References must follow a [specific format](/gateway/latest/plan-and-deploy/security/secrets-management/reference-format). | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Certificate for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print Certificate.to_json()

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_form_dict = certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


