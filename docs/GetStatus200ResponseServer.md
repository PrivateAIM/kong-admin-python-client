# GetStatus200ResponseServer

Metrics about the nginx HTTP/S server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections_reading** | **int** | The current number of connections where Kong is reading the request header. | [optional] 
**connections_writing** | **int** | The current number of connections where nginx is writing the response back to the client. | [optional] 
**total_requests** | **int** | The total number of client requests. | [optional] 
**connections_waiting** | **int** | The current number of idle client connections waiting for a request. | [optional] 
**connections_handled** | **int** | The total number of handled connections. Generally, the parameter value is the same as accepts unless some resource limits have been reached. | [optional] 
**connections_active** | **int** | The current number of active client connections including Waiting connections. | [optional] 
**connections_accepted** | **int** | The total number of accepted client connections. | [optional] 

## Example

```python
from kong_admin_client.models.get_status200_response_server import GetStatus200ResponseServer

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200ResponseServer from a JSON string
get_status200_response_server_instance = GetStatus200ResponseServer.from_json(json)
# print the JSON string representation of the object
print GetStatus200ResponseServer.to_json()

# convert the object into a dict
get_status200_response_server_dict = get_status200_response_server_instance.to_dict()
# create an instance of GetStatus200ResponseServer from a dict
get_status200_response_server_form_dict = get_status200_response_server.from_dict(get_status200_response_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


