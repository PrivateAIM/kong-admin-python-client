# FilterChainService

The service to which this chain is applied. A filter chain must be applied to either a single route or a single service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.filter_chain_service import FilterChainService

# TODO update the JSON string below
json = "{}"
# create an instance of FilterChainService from a JSON string
filter_chain_service_instance = FilterChainService.from_json(json)
# print the JSON string representation of the object
print FilterChainService.to_json()

# convert the object into a dict
filter_chain_service_dict = filter_chain_service_instance.to_dict()
# create an instance of FilterChainService from a dict
filter_chain_service_form_dict = filter_chain_service.from_dict(filter_chain_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


