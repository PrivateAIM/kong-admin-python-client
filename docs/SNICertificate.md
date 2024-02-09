# SNICertificate

The id (a UUID) of the certificate with which to associate the SNI hostname. The Certificate must have a valid private key associated with it to be used by the SNI object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.sni_certificate import SNICertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SNICertificate from a JSON string
sni_certificate_instance = SNICertificate.from_json(json)
# print the JSON string representation of the object
print SNICertificate.to_json()

# convert the object into a dict
sni_certificate_dict = sni_certificate_instance.to_dict()
# create an instance of SNICertificate from a dict
sni_certificate_form_dict = sni_certificate.from_dict(sni_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


