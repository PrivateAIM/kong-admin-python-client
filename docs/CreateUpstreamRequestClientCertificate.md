# CreateUpstreamRequestClientCertificate

If set, the certificate to be used as client certificate while TLS handshaking to the upstream server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_upstream_request_client_certificate import CreateUpstreamRequestClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpstreamRequestClientCertificate from a JSON string
create_upstream_request_client_certificate_instance = CreateUpstreamRequestClientCertificate.from_json(json)
# print the JSON string representation of the object
print CreateUpstreamRequestClientCertificate.to_json()

# convert the object into a dict
create_upstream_request_client_certificate_dict = create_upstream_request_client_certificate_instance.to_dict()
# create an instance of CreateUpstreamRequestClientCertificate from a dict
create_upstream_request_client_certificate_form_dict = create_upstream_request_client_certificate.from_dict(create_upstream_request_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


