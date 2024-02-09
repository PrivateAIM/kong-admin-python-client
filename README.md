# KongAdminClient
OpenAPI 3.0 spec for Kong Gateway's open source Admin API.

You can know more about Kong Gateway at [docs.konghq.com](https://docs.konghq.com)
.Give Kong a star at [Kong/kong](https://github.com/kong/kong) repository.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.5.0
- Package version: 3.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://konghq.com](https://konghq.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kong_admin_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kong_admin_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import kong_admin_client
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
    api_instance = kong_admin_client.CACertificatesApi(api_client)
    create_ca_certificate_request = kong_admin_client.CreateCaCertificateRequest() # CreateCaCertificateRequest | This request body represents a new Certificate Authority (CA) certificate and includes the properties required to create a new certificate. (optional)

    try:
        # Create a new CA certificate
        api_response = api_instance.create_ca_certificate(create_ca_certificate_request=create_ca_certificate_request)
        print("The response of CACertificatesApi->create_ca_certificate:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CACertificatesApi->create_ca_certificate: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8001*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CACertificatesApi* | [**create_ca_certificate**](docs/CACertificatesApi.md#create_ca_certificate) | **POST** /ca_certificates | Create a new CA certificate
*CACertificatesApi* | [**delete_ca_certificate**](docs/CACertificatesApi.md#delete_ca_certificate) | **DELETE** /ca_certificates/{ca_certificate_id} | Delete a CA Certificate
*CACertificatesApi* | [**get_ca_certificate**](docs/CACertificatesApi.md#get_ca_certificate) | **GET** /ca_certificates/{ca_certificate_id} | Fetch a CA certificate
*CACertificatesApi* | [**list_ca_certificate**](docs/CACertificatesApi.md#list_ca_certificate) | **GET** /ca_certificates | List all CA certificates
*CACertificatesApi* | [**update_ca_certificate**](docs/CACertificatesApi.md#update_ca_certificate) | **PATCH** /ca_certificates/{ca_certificate_id} | Update a CA Certificate
*CACertificatesApi* | [**updatet_ca_certificate**](docs/CACertificatesApi.md#updatet_ca_certificate) | **PUT** /ca_certificates/{ca_certificate_id} | Update a CA Certificate
*CertificatesApi* | [**create_certificate**](docs/CertificatesApi.md#create_certificate) | **POST** /certificates | Create a new Certificate
*CertificatesApi* | [**delete_certificate**](docs/CertificatesApi.md#delete_certificate) | **DELETE** /certificates/{certificate_id} | Delete a Certificate
*CertificatesApi* | [**get_certificate**](docs/CertificatesApi.md#get_certificate) | **GET** /certificates/{certificate_id} | Fetch a Certificate
*CertificatesApi* | [**list_certificate**](docs/CertificatesApi.md#list_certificate) | **GET** /certificates | List all certificates
*CertificatesApi* | [**update_certificate**](docs/CertificatesApi.md#update_certificate) | **PATCH** /certificates/{certificate_id} | Update a Certificate
*CertificatesApi* | [**update_certificate_put**](docs/CertificatesApi.md#update_certificate_put) | **PUT** /certificates/{certificate_id} | Update a Certificate
*ConsumersApi* | [**create_consumer**](docs/ConsumersApi.md#create_consumer) | **POST** /consumers | Create a new Consumer
*ConsumersApi* | [**delete_consumer**](docs/ConsumersApi.md#delete_consumer) | **DELETE** /consumers/{consumer_username_or_id} | Delete a Consumer
*ConsumersApi* | [**get_consumer**](docs/ConsumersApi.md#get_consumer) | **GET** /consumers/{consumer_username_or_id} | Fetch a Consumer
*ConsumersApi* | [**list_consumer**](docs/ConsumersApi.md#list_consumer) | **GET** /consumers | List all Consumers
*ConsumersApi* | [**update_consumer**](docs/ConsumersApi.md#update_consumer) | **PATCH** /consumers/{consumer_username_or_id} | Update a Consumer
*ConsumersApi* | [**upsert_consumer**](docs/ConsumersApi.md#upsert_consumer) | **PUT** /consumers/{consumer_username_or_id} | Update a Consumer
*DebugApi* | [**get_debug_node_log_level**](docs/DebugApi.md#get_debug_node_log_level) | **GET** /debug/node/log-level | Retrieve Node Log Level of A Node
*DebugApi* | [**put_debug_cluster_control_planes_nodes_log_level_log_level**](docs/DebugApi.md#put_debug_cluster_control_planes_nodes_log_level_log_level) | **PUT** /debug/cluster/control-planes-nodes/log-level/{log_level} | Set Node Log Level of All Control Plane Nodes
*DebugApi* | [**put_debug_cluster_log_level_log_level**](docs/DebugApi.md#put_debug_cluster_log_level_log_level) | **PUT** /debug/cluster/log-level/{log_level} | Set Node Log Level of All Nodes
*DebugApi* | [**put_debug_node_log_level_log_level**](docs/DebugApi.md#put_debug_node_log_level_log_level) | **PUT** /debug/node/log-level/{log_level} | Set log level of a single node
*InformationApi* | [**get_endpoints**](docs/InformationApi.md#get_endpoints) | **GET** /endpoints | List all endpoints
*InformationApi* | [**get_schemas_entity**](docs/InformationApi.md#get_schemas_entity) | **GET** /schemas/{entity}/validate | Retrieve entity schema
*InformationApi* | [**get_schemas_filters_filter_name**](docs/InformationApi.md#get_schemas_filters_filter_name) | **GET** /schemas/filters/{filter_name} | Retrieve Proxy-Wasm Filter JSON Schema
*InformationApi* | [**get_schemas_plugins_plugin_name**](docs/InformationApi.md#get_schemas_plugins_plugin_name) | **GET** /schemas/plugins/{plugin_name} | Retrieve Plugin Schema
*InformationApi* | [**get_schemas_vaults_vault_name**](docs/InformationApi.md#get_schemas_vaults_vault_name) | **GET** /schemas/vaults/{vault_name} | Retrieve Vault Schema
*InformationApi* | [**get_status**](docs/InformationApi.md#get_status) | **GET** /status | Health Routes
*InformationApi* | [**get_timers**](docs/InformationApi.md#get_timers) | **GET** /timers | Retrieve Runtime Debugging Info of Kong&#39;s Timers
*InformationApi* | [**head_endpoints**](docs/InformationApi.md#head_endpoints) | **HEAD** /{endpoint} | Check endpoint or entity existence
*InformationApi* | [**options_endpoint**](docs/InformationApi.md#options_endpoint) | **OPTIONS** /{endpoint} | List method by endpoint
*InformationApi* | [**post_schemas_entity_validate**](docs/InformationApi.md#post_schemas_entity_validate) | **POST** /schemas/{entity}/validate | Validate a configuration against a schema
*InformationApi* | [**post_schemas_plugins_validate**](docs/InformationApi.md#post_schemas_plugins_validate) | **POST** /schemas/plugins/validate | Validate plugin schema
*KeySetsApi* | [**create_key_set**](docs/KeySetsApi.md#create_key_set) | **POST** /key-sets | Create a new Key-set
*KeySetsApi* | [**delete_key_set**](docs/KeySetsApi.md#delete_key_set) | **DELETE** /key-sets/{key-set_id_or_name} | Delete a Key-set
*KeySetsApi* | [**get_key_set**](docs/KeySetsApi.md#get_key_set) | **GET** /key-sets/{key-set_id_or_name} | Fetch a Key-set
*KeySetsApi* | [**list_key_set**](docs/KeySetsApi.md#list_key_set) | **GET** /key-sets | List all Key-sets
*KeySetsApi* | [**update_key_set**](docs/KeySetsApi.md#update_key_set) | **PATCH** /key-sets/{key-set_id_or_name} | Update a Key-set
*KeySetsApi* | [**upsert_key_set**](docs/KeySetsApi.md#upsert_key_set) | **PUT** /key-sets/{key-set_id_or_name} | Update a Key-set
*KeysApi* | [**create_key**](docs/KeysApi.md#create_key) | **POST** /keys | Create a new Key
*KeysApi* | [**delete_key**](docs/KeysApi.md#delete_key) | **DELETE** /keys/{key_id_or_name} | Delete a Key
*KeysApi* | [**get_key**](docs/KeysApi.md#get_key) | **GET** /keys/{key_id_or_name} | Fetch a Key
*KeysApi* | [**list_key**](docs/KeysApi.md#list_key) | **GET** /keys | List all Keys
*KeysApi* | [**update_key**](docs/KeysApi.md#update_key) | **PATCH** /keys/{key_id_or_name} | Update a Key
*KeysApi* | [**upsert_key**](docs/KeysApi.md#upsert_key) | **PUT** /keys/{key_id_or_name} | Upsert a Key
*PluginsApi* | [**create_plugin**](docs/PluginsApi.md#create_plugin) | **POST** /plugins | Create a new Plugin
*PluginsApi* | [**create_plugin_for_consumer**](docs/PluginsApi.md#create_plugin_for_consumer) | **POST** /consumers/{consumer_username_or_id}/plugins | Create a new Plugin associated with a Consumer
*PluginsApi* | [**create_plugin_for_route**](docs/PluginsApi.md#create_plugin_for_route) | **POST** /routes/{route_id_or_name}/plugins | Create a new Plugin associated with a route
*PluginsApi* | [**create_plugin_for_service**](docs/PluginsApi.md#create_plugin_for_service) | **POST** /services/{service_id_or_name}plugins | Create a new Plugin associated with a service
*PluginsApi* | [**delete_plugin**](docs/PluginsApi.md#delete_plugin) | **DELETE** /plugins/{plugin_id} | Delete a Plugin
*PluginsApi* | [**delete_plugin_for_a_service**](docs/PluginsApi.md#delete_plugin_for_a_service) | **DELETE** /services/{service_id_or_name}/plugins/{plugin_id} | Delete a plugin associated with a service
*PluginsApi* | [**delete_plugin_for_consumer**](docs/PluginsApi.md#delete_plugin_for_consumer) | **DELETE** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Delete a Plugin associated with a Consumer
*PluginsApi* | [**delete_plugin_for_route**](docs/PluginsApi.md#delete_plugin_for_route) | **DELETE** /routes/{route_id_or_name}/plugins/{plugin_id} | Delete a Plugin associated with a route
*PluginsApi* | [**fetch_plugin_for_consumer**](docs/PluginsApi.md#fetch_plugin_for_consumer) | **GET** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Fetch a Plugin associated with a Consumer
*PluginsApi* | [**fetch_plugin_for_route**](docs/PluginsApi.md#fetch_plugin_for_route) | **GET** /routes/{route_id_or_name}/plugins/{plugin_id} | Fetch a Plugin associated with a route
*PluginsApi* | [**fetch_plugin_with_a_service**](docs/PluginsApi.md#fetch_plugin_with_a_service) | **GET** /services/{service_id_or_name}/plugins/{plugin_id} | Fetch a Plugin associated with a service
*PluginsApi* | [**get_plugin**](docs/PluginsApi.md#get_plugin) | **GET** /plugins/{plugin_id} | Fetch a Plugin
*PluginsApi* | [**get_plugins_for_service**](docs/PluginsApi.md#get_plugins_for_service) | **GET** /services/{service_id_or_name}plugins | List all Plugins associated with a service
*PluginsApi* | [**list_plugin**](docs/PluginsApi.md#list_plugin) | **GET** /plugins | List all Plugins
*PluginsApi* | [**list_plugins_for_consumer**](docs/PluginsApi.md#list_plugins_for_consumer) | **GET** /consumers/{consumer_username_or_id}/plugins | List all plugins associated with a consumer
*PluginsApi* | [**list_plugins_for_route**](docs/PluginsApi.md#list_plugins_for_route) | **GET** /routes/{route_id_or_name}/plugins | List all Plugins associated with a route
*PluginsApi* | [**update_plugin**](docs/PluginsApi.md#update_plugin) | **PATCH** /plugins/{plugin_id} | Update a Plugin
*PluginsApi* | [**update_plugin_for_a_service**](docs/PluginsApi.md#update_plugin_for_a_service) | **PATCH** /services/{service_id_or_name}/plugins/{plugin_id} | Update a plugin associated with a service
*PluginsApi* | [**update_plugin_for_consumer**](docs/PluginsApi.md#update_plugin_for_consumer) | **PATCH** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Update a Plugin associated with a Consumer
*PluginsApi* | [**update_plugin_for_route**](docs/PluginsApi.md#update_plugin_for_route) | **PATCH** /routes/{route_id_or_name}/plugins/{plugin_id} | Update a Plugin associated with a route
*PluginsApi* | [**upsert_plugin**](docs/PluginsApi.md#upsert_plugin) | **PUT** /plugins/{plugin_id} | Upsert a Plugin
*PluginsApi* | [**upsert_plugin_for_a_service**](docs/PluginsApi.md#upsert_plugin_for_a_service) | **PUT** /services/{service_id_or_name}/plugins/{plugin_id} | Upsert a plugin associated with a service
*PluginsApi* | [**upsert_plugin_for_consumer**](docs/PluginsApi.md#upsert_plugin_for_consumer) | **PUT** /consumers/{consumer_username_or_id}/plugins/{plugin_id} | Upsert a Plugin associated with a Consumer
*PluginsApi* | [**upsert_plugin_for_route**](docs/PluginsApi.md#upsert_plugin_for_route) | **PUT** /routes/{route_id_or_name}/plugins/{plugin_id} | Upsert a Plugin associated with a route
*RoutesApi* | [**create_route**](docs/RoutesApi.md#create_route) | **POST** /routes | Create a new route
*RoutesApi* | [**create_route_for_service**](docs/RoutesApi.md#create_route_for_service) | **POST** /services/{service_id_or_name}/routes | Create a new route associated with a service
*RoutesApi* | [**delete_route**](docs/RoutesApi.md#delete_route) | **DELETE** /routes/{route_id_or_name} | Delete a route
*RoutesApi* | [**delete_route_for_service**](docs/RoutesApi.md#delete_route_for_service) | **DELETE** /services/{service_id_or_name}/routes/{route_id_or_name} | Delete a route associated with a service
*RoutesApi* | [**fetch_route_for_service**](docs/RoutesApi.md#fetch_route_for_service) | **GET** /services/{service_id_or_name}/routes/{route_id_or_name} | Fetch a route associated with a service
*RoutesApi* | [**get_route**](docs/RoutesApi.md#get_route) | **GET** /routes/{route_id_or_name} | Fetch a route
*RoutesApi* | [**list_route**](docs/RoutesApi.md#list_route) | **GET** /routes | List all routes
*RoutesApi* | [**list_routes_for_service**](docs/RoutesApi.md#list_routes_for_service) | **GET** /services/{service_id_or_name}/routes | List all routes associated with a service
*RoutesApi* | [**update_route**](docs/RoutesApi.md#update_route) | **PATCH** /routes/{route_id_or_name} | Update a route
*RoutesApi* | [**update_route_for_service**](docs/RoutesApi.md#update_route_for_service) | **PATCH** /services/{service_id_or_name}/routes/{route_id_or_name} | Update a route associated with a service
*RoutesApi* | [**upsert_route**](docs/RoutesApi.md#upsert_route) | **PUT** /routes/{route_id_or_name} | Update a route
*RoutesApi* | [**upsert_route_for_service**](docs/RoutesApi.md#upsert_route_for_service) | **PUT** /services/{service_id_or_name}/routes/{route_id_or_name} | Upsert a route associated with a service
*SNIsApi* | [**create_sni**](docs/SNIsApi.md#create_sni) | **POST** /snis | Create a new SNI
*SNIsApi* | [**create_sni_for_certificate**](docs/SNIsApi.md#create_sni_for_certificate) | **POST** /certificates/{certificate_name_or_id}/snis | Create a new SNI associated with a Certificate
*SNIsApi* | [**delete_sni**](docs/SNIsApi.md#delete_sni) | **DELETE** /snis/{sni_name_or_id} | Delete an SNI
*SNIsApi* | [**delete_sni_for_certificate**](docs/SNIsApi.md#delete_sni_for_certificate) | **DELETE** /certificates/{certificate_id}/snis/{sni_name_or_id} | Delete a an SNI associated with a Certificate
*SNIsApi* | [**fetch_sni_with_certificate**](docs/SNIsApi.md#fetch_sni_with_certificate) | **GET** /certificates/{certificate_id}/snis/{sni_name_or_id} | Fetch an SNI associated with a certificate
*SNIsApi* | [**get_sni**](docs/SNIsApi.md#get_sni) | **GET** /snis/{sni_name_or_id} | Fetch an SNI
*SNIsApi* | [**get_sni_with_certificate**](docs/SNIsApi.md#get_sni_with_certificate) | **GET** /certificates/{certificate_name_or_id}/snis | List SNIs associated with a certificate
*SNIsApi* | [**list_sni**](docs/SNIsApi.md#list_sni) | **GET** /snis | List all SNIs
*SNIsApi* | [**update_sni**](docs/SNIsApi.md#update_sni) | **PATCH** /snis/{sni_name_or_id} | Update an SNI
*SNIsApi* | [**update_sni_for_certificate**](docs/SNIsApi.md#update_sni_for_certificate) | **PATCH** /certificates/{certificate_id}/snis/{sni_name_or_id} | Update SNI associated to a certificate
*SNIsApi* | [**upsert_sni**](docs/SNIsApi.md#upsert_sni) | **PUT** /snis/{sni_name_or_id} | Update an SNI
*SNIsApi* | [**upsert_sni_for_certificate**](docs/SNIsApi.md#upsert_sni_for_certificate) | **PUT** /certificates/{certificate_id}/snis/{sni_name_or_id} | Upsert an SNI associated with a certificate
*ServicesApi* | [**create_service**](docs/ServicesApi.md#create_service) | **POST** /services | Create a new service
*ServicesApi* | [**delete_service**](docs/ServicesApi.md#delete_service) | **DELETE** /services/{service_id_or_name} | Delete a service
*ServicesApi* | [**get_service**](docs/ServicesApi.md#get_service) | **GET** /services/{service_id_or_name} | Fetch a service
*ServicesApi* | [**list_service**](docs/ServicesApi.md#list_service) | **GET** /services | List all services
*ServicesApi* | [**update_service**](docs/ServicesApi.md#update_service) | **PATCH** /services/{service_id_or_name} | Update a service
*ServicesApi* | [**upsert_service**](docs/ServicesApi.md#upsert_service) | **PUT** /services/{service_id_or_name} | Upsert a service
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags | List all tags
*TagsApi* | [**get_tags_tags**](docs/TagsApi.md#get_tags_tags) | **GET** /tags/{tags} | List entity by tag
*TargetsApi* | [**create_target_for_upstream**](docs/TargetsApi.md#create_target_for_upstream) | **POST** /upstreams/{upstream_id_or_name}/targets | Create a new Target associated with an Upstream
*TargetsApi* | [**delete_upstream_target**](docs/TargetsApi.md#delete_upstream_target) | **DELETE** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Delete a Target associated with a an Upstream
*TargetsApi* | [**fetch_target_for_upstream**](docs/TargetsApi.md#fetch_target_for_upstream) | **GET** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Fetch a Target associated with an Upstream
*TargetsApi* | [**list_targets_for_upstream**](docs/TargetsApi.md#list_targets_for_upstream) | **GET** /upstreams/{upstream_id_or_name}/targets | List all Targets associated with an Upstream
*TargetsApi* | [**update_target_for_upstream**](docs/TargetsApi.md#update_target_for_upstream) | **PATCH** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Update a target associated with an Upstream
*TargetsApi* | [**upsert_target_for_upstream**](docs/TargetsApi.md#upsert_target_for_upstream) | **PUT** /upstreams/{upstream_id_or_name}/targets/{target_id_or_target} | Upsert a Target associated with an Upstream
*UpstreamsApi* | [**create_upstream**](docs/UpstreamsApi.md#create_upstream) | **POST** /upstreams | Create a new Upstream
*UpstreamsApi* | [**delete_upstream**](docs/UpstreamsApi.md#delete_upstream) | **DELETE** /upstreams/{upstream_id_or_name} | Delete an Upstream
*UpstreamsApi* | [**get_upstream**](docs/UpstreamsApi.md#get_upstream) | **GET** /upstreams/{upstream_id_or_name} | Fetch an Upstream
*UpstreamsApi* | [**list_upstream**](docs/UpstreamsApi.md#list_upstream) | **GET** /upstreams | List all Upstreams
*UpstreamsApi* | [**update_upstream**](docs/UpstreamsApi.md#update_upstream) | **PATCH** /upstreams/{upstream_id_or_name} | Update an Upstream
*UpstreamsApi* | [**upsert_upstream**](docs/UpstreamsApi.md#upsert_upstream) | **PUT** /upstreams/{upstream_id_or_name} | Update an Upstream
*VaultsApi* | [**create_vault**](docs/VaultsApi.md#create_vault) | **POST** /vaults | Create a new Vault
*VaultsApi* | [**delete_vault**](docs/VaultsApi.md#delete_vault) | **DELETE** /vaults/{vault_id_or_prefix} | Delete a Vault
*VaultsApi* | [**get_vault**](docs/VaultsApi.md#get_vault) | **GET** /vaults/{vault_id_or_prefix} | Fetch a Vault
*VaultsApi* | [**list_vault**](docs/VaultsApi.md#list_vault) | **GET** /vaults | List all Vaults
*VaultsApi* | [**update_vault**](docs/VaultsApi.md#update_vault) | **PATCH** /vaults/{vault_id_or_prefix} | Update a Vault
*VaultsApi* | [**upsert_vault**](docs/VaultsApi.md#upsert_vault) | **PUT** /vaults/{vault_id_or_prefix} | Upsert a Vault


## Documentation For Models

 - [CACertificate](docs/CACertificate.md)
 - [Certificate](docs/Certificate.md)
 - [Consumer](docs/Consumer.md)
 - [CreateCaCertificateRequest](docs/CreateCaCertificateRequest.md)
 - [CreateCertificateRequest](docs/CreateCertificateRequest.md)
 - [CreateConsumerRequest](docs/CreateConsumerRequest.md)
 - [CreateKeyRequest](docs/CreateKeyRequest.md)
 - [CreateKeyRequestPem](docs/CreateKeyRequestPem.md)
 - [CreateKeyRequestSet](docs/CreateKeyRequestSet.md)
 - [CreateKeySetRequest](docs/CreateKeySetRequest.md)
 - [CreatePluginForConsumerRequest](docs/CreatePluginForConsumerRequest.md)
 - [CreateRouteRequest](docs/CreateRouteRequest.md)
 - [CreateRouteRequestDestinationsInner](docs/CreateRouteRequestDestinationsInner.md)
 - [CreateRouteRequestHeaders](docs/CreateRouteRequestHeaders.md)
 - [CreateRouteRequestService](docs/CreateRouteRequestService.md)
 - [CreateRouteRequestSourcesInner](docs/CreateRouteRequestSourcesInner.md)
 - [CreateServiceRequest](docs/CreateServiceRequest.md)
 - [CreateServiceRequestClientCertificate](docs/CreateServiceRequestClientCertificate.md)
 - [CreateSniForCertificateRequest](docs/CreateSniForCertificateRequest.md)
 - [CreateSniForCertificateRequestCertificate](docs/CreateSniForCertificateRequestCertificate.md)
 - [CreateTargetForUpstreamRequest](docs/CreateTargetForUpstreamRequest.md)
 - [CreateTargetForUpstreamRequestUpstream](docs/CreateTargetForUpstreamRequestUpstream.md)
 - [CreateUpstreamRequest](docs/CreateUpstreamRequest.md)
 - [CreateUpstreamRequestClientCertificate](docs/CreateUpstreamRequestClientCertificate.md)
 - [CreateUpstreamRequestHealthchecks](docs/CreateUpstreamRequestHealthchecks.md)
 - [CreateUpstreamRequestHealthchecksActive](docs/CreateUpstreamRequestHealthchecksActive.md)
 - [CreateUpstreamRequestHealthchecksActiveHealthy](docs/CreateUpstreamRequestHealthchecksActiveHealthy.md)
 - [CreateUpstreamRequestHealthchecksActiveUnhealthy](docs/CreateUpstreamRequestHealthchecksActiveUnhealthy.md)
 - [CreateUpstreamRequestHealthchecksPassive](docs/CreateUpstreamRequestHealthchecksPassive.md)
 - [CreateUpstreamRequestHealthchecksPassiveHealthy](docs/CreateUpstreamRequestHealthchecksPassiveHealthy.md)
 - [CreateUpstreamRequestHealthchecksPassiveUnhealthy](docs/CreateUpstreamRequestHealthchecksPassiveUnhealthy.md)
 - [CreateVaultRequest](docs/CreateVaultRequest.md)
 - [CreateVaultRequestConfig](docs/CreateVaultRequestConfig.md)
 - [FilterChain](docs/FilterChain.md)
 - [FilterChainFiltersInner](docs/FilterChainFiltersInner.md)
 - [FilterChainFiltersInnerConfig](docs/FilterChainFiltersInnerConfig.md)
 - [FilterChainRoute](docs/FilterChainRoute.md)
 - [FilterChainService](docs/FilterChainService.md)
 - [GetDebugNodeLogLevel200Response](docs/GetDebugNodeLogLevel200Response.md)
 - [GetEndpoints200Response](docs/GetEndpoints200Response.md)
 - [GetSchemasEntity200Response](docs/GetSchemasEntity200Response.md)
 - [GetSchemasEntity200ResponseFieldsInner](docs/GetSchemasEntity200ResponseFieldsInner.md)
 - [GetSchemasEntity200ResponseFieldsInnerId](docs/GetSchemasEntity200ResponseFieldsInnerId.md)
 - [GetSniWithCertificate200Response](docs/GetSniWithCertificate200Response.md)
 - [GetSniWithCertificate200ResponseDataInner](docs/GetSniWithCertificate200ResponseDataInner.md)
 - [GetSniWithCertificate200ResponseDataInnerCertificate](docs/GetSniWithCertificate200ResponseDataInnerCertificate.md)
 - [GetStatus200Response](docs/GetStatus200Response.md)
 - [GetStatus200ResponseDatabase](docs/GetStatus200ResponseDatabase.md)
 - [GetStatus200ResponseMemory](docs/GetStatus200ResponseMemory.md)
 - [GetStatus200ResponseMemoryLuaSharedDicts](docs/GetStatus200ResponseMemoryLuaSharedDicts.md)
 - [GetStatus200ResponseMemoryLuaSharedDictsKongCoreDbCache](docs/GetStatus200ResponseMemoryLuaSharedDictsKongCoreDbCache.md)
 - [GetStatus200ResponseMemoryWorkersLuaVmsInner](docs/GetStatus200ResponseMemoryWorkersLuaVmsInner.md)
 - [GetStatus200ResponseServer](docs/GetStatus200ResponseServer.md)
 - [GetTags200Response](docs/GetTags200Response.md)
 - [GetTags200ResponseDataInner](docs/GetTags200ResponseDataInner.md)
 - [GetTimers200Response](docs/GetTimers200Response.md)
 - [GetTimers200ResponseStats](docs/GetTimers200ResponseStats.md)
 - [GetTimers200ResponseStatsFlamegraph](docs/GetTimers200ResponseStatsFlamegraph.md)
 - [GetTimers200ResponseStatsSys](docs/GetTimers200ResponseStatsSys.md)
 - [GetTimers200ResponseStatsTimers](docs/GetTimers200ResponseStatsTimers.md)
 - [GetTimers200ResponseStatsTimersMeta](docs/GetTimers200ResponseStatsTimersMeta.md)
 - [GetTimers200ResponseWorker](docs/GetTimers200ResponseWorker.md)
 - [Key](docs/Key.md)
 - [KeyPem](docs/KeyPem.md)
 - [KeySet](docs/KeySet.md)
 - [ListCertificate200Response](docs/ListCertificate200Response.md)
 - [ListConsumer200Response](docs/ListConsumer200Response.md)
 - [ListKey200Response](docs/ListKey200Response.md)
 - [ListKeySet200Response](docs/ListKeySet200Response.md)
 - [ListPluginsForConsumer200Response](docs/ListPluginsForConsumer200Response.md)
 - [ListPluginsForConsumer200ResponseConfig](docs/ListPluginsForConsumer200ResponseConfig.md)
 - [ListPluginsForConsumer200ResponseOrdering](docs/ListPluginsForConsumer200ResponseOrdering.md)
 - [ListPluginsForRoute200Response](docs/ListPluginsForRoute200Response.md)
 - [ListRoute200Response](docs/ListRoute200Response.md)
 - [ListService200Response](docs/ListService200Response.md)
 - [ListTargetsForUpstream200Response](docs/ListTargetsForUpstream200Response.md)
 - [ListUpstream200Response](docs/ListUpstream200Response.md)
 - [ListVault200Response](docs/ListVault200Response.md)
 - [Plugin](docs/Plugin.md)
 - [PluginConsumer](docs/PluginConsumer.md)
 - [PluginRoute](docs/PluginRoute.md)
 - [PluginService](docs/PluginService.md)
 - [PostSchemasEntityValidate200Response](docs/PostSchemasEntityValidate200Response.md)
 - [PostSchemasPluginsValidate200Response](docs/PostSchemasPluginsValidate200Response.md)
 - [PutDebugClusterControlPlanesNodesLogLevelLogLevel200Response](docs/PutDebugClusterControlPlanesNodesLogLevelLogLevel200Response.md)
 - [PutDebugClusterLogLevelLogLevel200Response](docs/PutDebugClusterLogLevelLogLevel200Response.md)
 - [PutDebugNodeLogLevelLogLevel200Response](docs/PutDebugNodeLogLevelLogLevel200Response.md)
 - [Route](docs/Route.md)
 - [RouteDestinationsInner](docs/RouteDestinationsInner.md)
 - [RouteService](docs/RouteService.md)
 - [SNI](docs/SNI.md)
 - [SNICertificate](docs/SNICertificate.md)
 - [Service](docs/Service.md)
 - [ServiceClientCertificate](docs/ServiceClientCertificate.md)
 - [Target](docs/Target.md)
 - [TargetUpstream](docs/TargetUpstream.md)
 - [UpsertConsumer200Response](docs/UpsertConsumer200Response.md)
 - [UpsertConsumer200ResponseDataInner](docs/UpsertConsumer200ResponseDataInner.md)
 - [Upstream](docs/Upstream.md)
 - [UpstreamClientCertificate](docs/UpstreamClientCertificate.md)
 - [UpstreamHealthchecks](docs/UpstreamHealthchecks.md)
 - [UpstreamHealthchecksActive](docs/UpstreamHealthchecksActive.md)
 - [UpstreamHealthchecksActiveHealthy](docs/UpstreamHealthchecksActiveHealthy.md)
 - [UpstreamHealthchecksActiveUnhealthy](docs/UpstreamHealthchecksActiveUnhealthy.md)
 - [UpstreamHealthchecksPassive](docs/UpstreamHealthchecksPassive.md)
 - [UpstreamHealthchecksPassiveHealthy](docs/UpstreamHealthchecksPassiveHealthy.md)
 - [UpstreamHealthchecksPassiveUnhealthy](docs/UpstreamHealthchecksPassiveUnhealthy.md)
 - [Vault](docs/Vault.md)
 - [VaultConfig](docs/VaultConfig.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

docs@konghq.com

