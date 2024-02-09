# SNI

An SNI object represents a many-to-one mapping of hostnames to a certificate. That is, a certificate object can have many hostnames associated with it; when Kong receives an SSL request, it uses the SNI field in the Client Hello to lookup the certificate object based on the SNI associated with the certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**SNICertificate**](SNICertificate.md) |  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The SNI name to associate with the given certificate. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the SNIs for grouping and filtering. | [optional] 

## Example

```python
from kong_admin_client.models.sni import SNI

# TODO update the JSON string below
json = "{}"
# create an instance of SNI from a JSON string
sni_instance = SNI.from_json(json)
# print the JSON string representation of the object
print SNI.to_json()

# convert the object into a dict
sni_dict = sni_instance.to_dict()
# create an instance of SNI from a dict
sni_form_dict = sni.from_dict(sni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


