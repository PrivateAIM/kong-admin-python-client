# FilterChainFiltersInnerConfig

The configuration for the filter. Proxy-Wasm does not define a configuration format, so this field accepts either a raw string, or a JSON object. A raw string is passed uninterpreted to the filter, to be validated at request time. If a JSON object is used, there must be a metadata file called `my-filter.meta.json` in the same folder as your `my-filter.wasm` file. The metadata file must contain an object with a field `\"config_schema\"`, and its value must the JSON Schema for the filter configuration. This schema will be used for validating the configuration upon insertion in the filter chain, ahead of execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from kong_admin_client.models.filter_chain_filters_inner_config import FilterChainFiltersInnerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FilterChainFiltersInnerConfig from a JSON string
filter_chain_filters_inner_config_instance = FilterChainFiltersInnerConfig.from_json(json)
# print the JSON string representation of the object
print FilterChainFiltersInnerConfig.to_json()

# convert the object into a dict
filter_chain_filters_inner_config_dict = filter_chain_filters_inner_config_instance.to_dict()
# create an instance of FilterChainFiltersInnerConfig from a dict
filter_chain_filters_inner_config_form_dict = filter_chain_filters_inner_config.from_dict(filter_chain_filters_inner_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


