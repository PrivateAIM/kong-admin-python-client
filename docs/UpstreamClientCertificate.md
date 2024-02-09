# UpstreamClientCertificate

If set, the certificate to be used as client certificate while TLS handshaking to the upstream server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.upstream_client_certificate import UpstreamClientCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of UpstreamClientCertificate from a JSON string
upstream_client_certificate_instance = UpstreamClientCertificate.from_json(json)
# print the JSON string representation of the object
print UpstreamClientCertificate.to_json()

# convert the object into a dict
upstream_client_certificate_dict = upstream_client_certificate_instance.to_dict()
# create an instance of UpstreamClientCertificate from a dict
upstream_client_certificate_form_dict = upstream_client_certificate.from_dict(upstream_client_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


