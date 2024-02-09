# CreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The service name.  | [optional] 
**retries** | **int** | The number of retries to execute upon failure to proxy. Default:&#x60;5&#x60;.  | [optional] [default to 5]
**protocol** | **str** | The protocol used to communicate with the upstream. Accepted values are: \&quot;&#x60;grpc&#x60;\&quot;, \&quot;&#x60;grpcs&#x60;\&quot;, \&quot;&#x60;http&#x60;\&quot;, \&quot;&#x60;https&#x60;\&quot;, \&quot;&#x60;tcp&#x60;\&quot;, \&quot;&#x60;tls&#x60;\&quot;, \&quot;&#x60;tls_passthrough&#x60;\&quot;, \&quot;&#x60;udp&#x60;\&quot;, \&quot;&#x60;ws&#x60;\&quot; , \&quot;&#x60;wss&#x60;\&quot; . Default: \&quot;&#x60;http&#x60;\&quot;. | [default to 'http']
**host** | **str** | The host of the upstream server. Note that the host value is case sensitive.  | 
**port** | **int** | The upstream server port. Default: &#x60;80&#x60;.  | [default to 80]
**path** | **str** | The path to be used in requests to the upstream server.  | [optional] 
**connect_timeout** | **int** | The timeout in milliseconds for establishing a connection to the upstream server. | [optional] [default to 6000]
**write_timeout** | **int** | The timeout in milliseconds between two successive write operations for transmitting a request to the upstream server. Default: &#x60;60000&#x60;.  | [optional] [default to 6000]
**read_timeout** | **int** | The timeout in milliseconds between two successive read operations for transmitting a request to the upstream server. Default: &#x60;60000&#x60;.  | [optional] [default to 6000]
**tags** | **List[str]** | An optional set of strings associated with the service for grouping and filtering.  | [optional] 
**client_certificate** | [**CreateServiceRequestClientCertificate**](CreateServiceRequestClientCertificate.md) |  | [optional] 
**tls_verify** | **bool** | Whether to enable verification of upstream server TLS certificate. If set to null, then the Nginx default is respected.  | [optional] [default to True]
**tls_verify_depth** | **str** | Maximum depth of chain while verifying Upstream server&#39;s TLS certificate. If set to null, then the Nginx default is respected. Default: null.  | [optional] 
**ca_certificates** | **List[str]** | Array of CA Certificate object UUIDs that are used to build the trust store while verifying upstream server&#39;s TLS certificate. If set to null when Nginx default is respected.  With form-encoded, the notation is &#x60;ca_certificates[]&#x3D;4e3ad2e4-0bc4-4638-8e34-c84a417ba39b&amp;ca_certificates[]&#x3D;51e77dc2-8f3e-4afa-9d0e-0e3bbbcfd515&#x60;. With JSON, use an Array.  | [optional] 
**enabled** | **bool** | Whether the service is active. If set to &#x60;false&#x60;, the proxy behavior will be as if any routes attached to it do not exist (404). Default: &#x60;true&#x60;.  | [default to True]

## Example

```python
from kong_admin_client.models.create_service_request import CreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceRequest from a JSON string
create_service_request_instance = CreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print CreateServiceRequest.to_json()

# convert the object into a dict
create_service_request_dict = create_service_request_instance.to_dict()
# create an instance of CreateServiceRequest from a dict
create_service_request_form_dict = create_service_request.from_dict(create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


