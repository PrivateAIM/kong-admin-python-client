# CreateVaultRequestConfig

The configuration properties for the Vault which can be found on the vaults' documentation page. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.create_vault_request_config import CreateVaultRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVaultRequestConfig from a JSON string
create_vault_request_config_instance = CreateVaultRequestConfig.from_json(json)
# print the JSON string representation of the object
print CreateVaultRequestConfig.to_json()

# convert the object into a dict
create_vault_request_config_dict = create_vault_request_config_instance.to_dict()
# create an instance of CreateVaultRequestConfig from a dict
create_vault_request_config_form_dict = create_vault_request_config.from_dict(create_vault_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


