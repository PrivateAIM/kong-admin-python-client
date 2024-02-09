# CACertificate

A CA certificate object represents a trusted CA. These objects are used by Kong to verify the validity of a client or server certificate. CA Certificates can be both tagged and filtered by tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert** | **str** | PEM-encoded public certificate of the CA. | [optional] 
**cert_digest** | **str** | SHA256 hex digest of the public certificate. | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**id** | **str** |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Certificate for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.ca_certificate import CACertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CACertificate from a JSON string
ca_certificate_instance = CACertificate.from_json(json)
# print the JSON string representation of the object
print CACertificate.to_json()

# convert the object into a dict
ca_certificate_dict = ca_certificate_instance.to_dict()
# create an instance of CACertificate from a dict
ca_certificate_form_dict = ca_certificate.from_dict(ca_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


