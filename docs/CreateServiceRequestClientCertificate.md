# CreateServiceRequestClientCertificate

Certificate to be used as client certificate while TLS handshaking to the upstream server. With form-encoded, the notation is `client_certificate.id=<client_certificate id>`. With JSON, use `\"client_certificate\":{\"id\":\"<client_certificate id>\"}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_service_request_client_certificate import CreateServiceRequestClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceRequestClientCertificate from a JSON string
create_service_request_client_certificate_instance = CreateServiceRequestClientCertificate.from_json(json)
# print the JSON string representation of the object
print CreateServiceRequestClientCertificate.to_json()

# convert the object into a dict
create_service_request_client_certificate_dict = create_service_request_client_certificate_instance.to_dict()
# create an instance of CreateServiceRequestClientCertificate from a dict
create_service_request_client_certificate_form_dict = create_service_request_client_certificate.from_dict(create_service_request_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


