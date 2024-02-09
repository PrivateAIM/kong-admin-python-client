# FilterChain

A Filter Chain entity represents a list of one or more WebAssembly filters that will be executed during the HTTP request/response lifecycle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**enabled** | **bool** | Whether the filter chain is applied. | [optional] 
**filters** | [**List[FilterChainFiltersInner]**](FilterChainFiltersInner.md) | An array of filter definitions that will be executed in order. | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The name of the filter chain. | [optional] 
**route** | [**FilterChainRoute**](FilterChainRoute.md) |  | [optional] 
**service** | [**FilterChainService**](FilterChainService.md) |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Filter Chain for grouping and filtering. | [optional] 
**updated_at** | **int** | Unix epoch when the resource was last updated. | [optional] 

## Example

```python
from kong_admin_client.models.filter_chain import FilterChain

# TODO update the JSON string below
json = "{}"
# create an instance of FilterChain from a JSON string
filter_chain_instance = FilterChain.from_json(json)
# print the JSON string representation of the object
print FilterChain.to_json()

# convert the object into a dict
filter_chain_dict = filter_chain_instance.to_dict()
# create an instance of FilterChain from a dict
filter_chain_form_dict = filter_chain.from_dict(filter_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


