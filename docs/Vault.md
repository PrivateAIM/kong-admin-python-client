# Vault

Vault entities are used to configure different Vault connectors. Examples of Vaults are Environment Variables, Hashicorp Vault and AWS Secrets Manager. Configuring a Vault allows referencing the secrets with other entities. For example a certificate entity can store a reference to a certificate and key, stored in a vault, instead of storing the certificate and key within the entity. This allows a proper separation of secrets and configuration and prevents secret sprawl.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**VaultConfig**](VaultConfig.md) |  | [optional] 
**created_at** | **int** | Unix epoch when the resource was created. | [optional] 
**description** | **str** | The description of the Vault entity. | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** | The name of the Vault thats going to be added. Currently, the Vault implementation must be installed in every Kong instance. | [optional] 
**prefix** | **str** | The unique prefix (or identifier) for this Vault configuration. The prefix is used to load the right Vault configuration and implementation when referencing secrets with the other entities. | [optional] 
**tags** | **List[str]** | An optional set of strings associated with the Vault for grouping and filtering. | [optional] 
**updated_at** | **int** | Unix epoch when the resource was last updated. | [optional] 

## Example

```python
from kong_admin_client.models.vault import Vault

# TODO update the JSON string below
json = "{}"
# create an instance of Vault from a JSON string
vault_instance = Vault.from_json(json)
# print the JSON string representation of the object
print Vault.to_json()

# convert the object into a dict
vault_dict = vault_instance.to_dict()
# create an instance of Vault from a dict
vault_form_dict = vault.from_dict(vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


