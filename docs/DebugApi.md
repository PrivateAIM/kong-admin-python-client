# kong_admin_client.DebugApi

All URIs are relative to *http://localhost:8001*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_debug_node_log_level**](DebugApi.md#get_debug_node_log_level) | **GET** /debug/node/log-level | Retrieve Node Log Level of A Node
[**put_debug_cluster_control_planes_nodes_log_level_log_level**](DebugApi.md#put_debug_cluster_control_planes_nodes_log_level_log_level) | **PUT** /debug/cluster/control-planes-nodes/log-level/{log_level} | Set Node Log Level of All Control Plane Nodes
[**put_debug_cluster_log_level_log_level**](DebugApi.md#put_debug_cluster_log_level_log_level) | **PUT** /debug/cluster/log-level/{log_level} | Set Node Log Level of All Nodes
[**put_debug_node_log_level_log_level**](DebugApi.md#put_debug_node_log_level_log_level) | **PUT** /debug/node/log-level/{log_level} | Set log level of a single node


# **get_debug_node_log_level**
> GetDebugNodeLogLevel200Response get_debug_node_log_level()

Retrieve Node Log Level of A Node

Retrieve the current log level of a node.  See the [NGINX documentation](http://nginx.org/en/docs/ngx_core_module.html#error_log) for the list of possible return values.

### Example


```python
import kong_admin_client
from kong_admin_client.models.get_debug_node_log_level200_response import GetDebugNodeLogLevel200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.DebugApi(api_client)

    try:
        # Retrieve Node Log Level of A Node
        api_response = api_instance.get_debug_node_log_level()
        print("The response of DebugApi->get_debug_node_log_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->get_debug_node_log_level: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDebugNodeLogLevel200Response**](GetDebugNodeLogLevel200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_debug_cluster_control_planes_nodes_log_level_log_level**
> PutDebugClusterControlPlanesNodesLogLevelLogLevel200Response put_debug_cluster_control_planes_nodes_log_level_log_level(log_level)

Set Node Log Level of All Control Plane Nodes

Change the log level of all Control Plane nodes deployed in Hybrid (CP/DP) cluster.  See the [NGINX docs](http://nginx.org/en/docs/ngx_core_module.html#error_log) for a list of accepted values.  Care must be taken when changing the log level of a node to `debug` in a production environment because the disk could fill up quickly. As soon as the debug logging finishes, revert back to a higher level such as notice.  It's currently not possible to change the log level of DP and DB-less nodes. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.put_debug_cluster_control_planes_nodes_log_level_log_level200_response import PutDebugClusterControlPlanesNodesLogLevelLogLevel200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.DebugApi(api_client)
    log_level = 'warn' # str | Log levels are set in Kong's configuration. Log levels increase in order of their severity

    try:
        # Set Node Log Level of All Control Plane Nodes
        api_response = api_instance.put_debug_cluster_control_planes_nodes_log_level_log_level(log_level)
        print("The response of DebugApi->put_debug_cluster_control_planes_nodes_log_level_log_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->put_debug_cluster_control_planes_nodes_log_level_log_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_level** | **str**| Log levels are set in Kong&#39;s configuration. Log levels increase in order of their severity | 

### Return type

[**PutDebugClusterControlPlanesNodesLogLevelLogLevel200Response**](PutDebugClusterControlPlanesNodesLogLevelLogLevel200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_debug_cluster_log_level_log_level**
> PutDebugClusterLogLevelLogLevel200Response put_debug_cluster_log_level_log_level(log_level)

Set Node Log Level of All Nodes

Change the log level of all nodes in a cluster.    See the [NGINX docs](http://nginx.org/en/docs/ngx_core_module.html#error_log) for a list of accepted values.  It's currently not possible to change the log level of DP and DB-less nodes.  Currently, when a user dynamically changes the log level for the entire cluster, if a new node joins a cluster the new node will run at the previous log level, not at the log level that was previously set dynamically for the entire cluster. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.put_debug_cluster_log_level_log_level200_response import PutDebugClusterLogLevelLogLevel200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.DebugApi(api_client)
    log_level = 'warn' # str | Log levels are set in Kong's configuration. Log levels increase in order of their severity

    try:
        # Set Node Log Level of All Nodes
        api_response = api_instance.put_debug_cluster_log_level_log_level(log_level)
        print("The response of DebugApi->put_debug_cluster_log_level_log_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->put_debug_cluster_log_level_log_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_level** | **str**| Log levels are set in Kong&#39;s configuration. Log levels increase in order of their severity | 

### Return type

[**PutDebugClusterLogLevelLogLevel200Response**](PutDebugClusterLogLevelLogLevel200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_debug_node_log_level_log_level**
> PutDebugNodeLogLevelLogLevel200Response put_debug_node_log_level_log_level(log_level)

Set log level of a single node

Change the log level of a node.  See the [NGINX documentation](http://nginx.org/en/docs/ngx_core_module.html#error_log) for the list of possible return values. 

### Example


```python
import kong_admin_client
from kong_admin_client.models.put_debug_node_log_level_log_level200_response import PutDebugNodeLogLevelLogLevel200Response
from kong_admin_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = kong_admin_client.Configuration(
    host = "http://localhost:8001"
)


# Enter a context with an instance of the API client
with kong_admin_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kong_admin_client.DebugApi(api_client)
    log_level = 'warn' # str | Log levels are set in Kong's configuration. Log levels increase in order of their severity

    try:
        # Set log level of a single node
        api_response = api_instance.put_debug_node_log_level_log_level(log_level)
        print("The response of DebugApi->put_debug_node_log_level_log_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DebugApi->put_debug_node_log_level_log_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_level** | **str**| Log levels are set in Kong&#39;s configuration. Log levels increase in order of their severity | 

### Return type

[**PutDebugNodeLogLevelLogLevel200Response**](PutDebugNodeLogLevelLogLevel200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

