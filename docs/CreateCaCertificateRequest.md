# CreateCaCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | PEM-encoded public certificate of the CA.  | 
**cert_digest** | **str** | SHA256 hex digest of the public certificate.  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Certificate for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.create_ca_certificate_request import CreateCaCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCaCertificateRequest from a JSON string
create_ca_certificate_request_instance = CreateCaCertificateRequest.from_json(json)
# print the JSON string representation of the object
print CreateCaCertificateRequest.to_json()

# convert the object into a dict
create_ca_certificate_request_dict = create_ca_certificate_request_instance.to_dict()
# create an instance of CreateCaCertificateRequest from a dict
create_ca_certificate_request_form_dict = create_ca_certificate_request.from_dict(create_ca_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


