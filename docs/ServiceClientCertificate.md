# ServiceClientCertificate

Certificate to be used as client certificate while TLS handshaking to the upstream server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.service_client_certificate import ServiceClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceClientCertificate from a JSON string
service_client_certificate_instance = ServiceClientCertificate.from_json(json)
# print the JSON string representation of the object
print ServiceClientCertificate.to_json()

# convert the object into a dict
service_client_certificate_dict = service_client_certificate_instance.to_dict()
# create an instance of ServiceClientCertificate from a dict
service_client_certificate_form_dict = service_client_certificate.from_dict(service_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


