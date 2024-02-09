# CreateCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | PEM-encoded public certificate chain of the SSL key pair. | 
**key** | **str** | PEM-encoded private key of the SSL key pair. | 
**cert_alt** | **str** | PEM-encoded public certificate chain of the alternate SSL key pair. | [optional] 
**key_alt** | **str** | PEM-encoded private key of the alternate SSL key pair. | [optional] 
**snis** | **List[str]** | An array of zero or more hostnames to associate with this certificate as SNIs. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Certificate for grouping and filtering.  | [optional] 
**passphrase** | **str** | To load an encrypted private key into Kong, specify the passphrase using this attributKong will decrypt the private key and store it in its database. e. Enterprise Only | [optional] 

## Example

```python
from kong_admin_client.models.create_certificate_request import CreateCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCertificateRequest from a JSON string
create_certificate_request_instance = CreateCertificateRequest.from_json(json)
# print the JSON string representation of the object
print CreateCertificateRequest.to_json()

# convert the object into a dict
create_certificate_request_dict = create_certificate_request_instance.to_dict()
# create an instance of CreateCertificateRequest from a dict
create_certificate_request_form_dict = create_certificate_request.from_dict(create_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


