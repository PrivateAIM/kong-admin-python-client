# VaultConfig

The configuration properties for the Vault which can be found on the [vaults' documentation page](https://docs.konghq.com/gateway/latest/kong-enterprise/secrets-management/advanced-usage/).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prefix** | **str** | The unique prefix (or identifier) for this Vault configuration. The prefix is used to load the right Vault configuration and implementation when referencing secrets with the other entities. | [optional] 

## Example

```python
from kong_admin_client.models.vault_config import VaultConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VaultConfig from a JSON string
vault_config_instance = VaultConfig.from_json(json)
# print the JSON string representation of the object
print VaultConfig.to_json()

# convert the object into a dict
vault_config_dict = vault_config_instance.to_dict()
# create an instance of VaultConfig from a dict
vault_config_form_dict = vault_config.from_dict(vault_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


