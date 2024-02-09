# Service

service entities are abstractions of upstream services. The main attribute of a service is its URL which can be set as a single string or by specifying the `protocol`, `host`, `port` and `path` individually.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificates** | **List[str]** | Array of &#x60;CA Certificate&#x60; object UUIDs that are used to build the trust store while verifying upstream server&#39;s TLS certificate. If set to &#x60;null&#x60; when Nginx default is respected. If default CA list in Nginx are not specified and TLS verification is enabled, then handshake with upstream server will always fail (because no CA are trusted). | [optional] 
**client_certificate** | [**ServiceClientCertificate**](ServiceClientCertificate.md) |  | [optional] 
**connect_timeout** | **int** | The timeout in milliseconds for establishing a connection to the upstream server. | [optional] [default to 60000]
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**enabled** | **bool** | Whether the service is active. If set to &#x60;false&#x60;, the proxy behavior will be as if any routes attached to it do not exist (404). | [optional] [default to True]
**host** | **str** | The host of the upstream server. Note that the host value is case sensitive. | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The service name. | [optional] 
**path** | **str** | The path to be used in requests to the upstream server. | [optional] 
**port** | **int** | The upstream server port. | [optional] [default to 80]
**protocol** | **str** | The protocol used to communicate with the upstream. | [optional] [default to 'http']
**read_timeout** | **int** | The timeout in milliseconds between two successive read operations for transmitting a request to the upstream server. | [optional] [default to 60000]
**retries** | **int** | The number of retries to execute upon failure to proxy. | [optional] [default to 5]
**tags** | **List[str]** | An optional set of strings associated with the service for grouping and filtering. | [optional] 
**tls_verify** | **bool** | Whether to enable verification of upstream server TLS certificate. If set to &#x60;null&#x60;, then the Nginx default is respected. | [optional] 
**tls_verify_depth** | **int** | Maximum depth of chain while verifying Upstream server&#39;s TLS certificate. If set to &#x60;null&#x60;, then the Nginx default is respected.&#39; | [optional] 
**updated_at** | **int** | Unix epoch when the resource was last updated. | [optional] 
**url** | **str** | Helper field to set &#x60;protocol&#x60;, &#x60;host&#x60;, &#x60;port&#x60; and &#x60;path&#x60; using a URL. This field is write-only and is not returned in responses. | [optional] 
**write_timeout** | **int** | The timeout in milliseconds between two successive write operations for transmitting a request to the upstream server. | [optional] [default to 60000]

## Example

```python
from kong_admin_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print Service.to_json()

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_form_dict = service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


