# GetStatus200ResponseDatabase

Metrics about the database

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reachable** | **bool** | A boolean value reflecting the state of the database connection. Please note that this flag does not reflect the health of the database itself. | [optional] 

## Example

```python
from kong_admin_client.models.get_status200_response_database import GetStatus200ResponseDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus200ResponseDatabase from a JSON string
get_status200_response_database_instance = GetStatus200ResponseDatabase.from_json(json)
# print the JSON string representation of the object
print GetStatus200ResponseDatabase.to_json()

# convert the object into a dict
get_status200_response_database_dict = get_status200_response_database_instance.to_dict()
# create an instance of GetStatus200ResponseDatabase from a dict
get_status200_response_database_form_dict = get_status200_response_database.from_dict(get_status200_response_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


