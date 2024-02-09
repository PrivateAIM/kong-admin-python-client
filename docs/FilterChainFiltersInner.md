# FilterChainFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the filter. This name matches the basename of the WebAssembly module file: for a filter file called &#x60;my-filter.wasm&#x60;, then filter name will be &#x60;my-filter&#x60;. | [optional] 
**config** | [**FilterChainFiltersInnerConfig**](FilterChainFiltersInnerConfig.md) |  | [optional] 
**enabled** | **bool** | Whether the filter is to be applied. | [optional] 

## Example

```python
from kong_admin_client.models.filter_chain_filters_inner import FilterChainFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of FilterChainFiltersInner from a JSON string
filter_chain_filters_inner_instance = FilterChainFiltersInner.from_json(json)
# print the JSON string representation of the object
print FilterChainFiltersInner.to_json()

# convert the object into a dict
filter_chain_filters_inner_dict = filter_chain_filters_inner_instance.to_dict()
# create an instance of FilterChainFiltersInner from a dict
filter_chain_filters_inner_form_dict = filter_chain_filters_inner.from_dict(filter_chain_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


