# CreateVaultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The unique prefix (or identifier) for this Vault configuration. The prefix is used to load the right Vault configuration and implementation when referencing secrets with the other entities.  | [optional] 
**name** | **str** | The name of the Vault that&#39;s going to be added. Currently, the Vault implementation must be installed in every Kong instance.  | [optional] 
**description** | **str** | The description of the Vault object.  | [optional] 
**config** | [**CreateVaultRequestConfig**](CreateVaultRequestConfig.md) |  | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Vault for grouping and filtering.  | [optional] 

## Example

```python
from kong_admin_client.models.create_vault_request import CreateVaultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVaultRequest from a JSON string
create_vault_request_instance = CreateVaultRequest.from_json(json)
# print the JSON string representation of the object
print CreateVaultRequest.to_json()

# convert the object into a dict
create_vault_request_dict = create_vault_request_instance.to_dict()
# create an instance of CreateVaultRequest from a dict
create_vault_request_form_dict = create_vault_request.from_dict(create_vault_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


