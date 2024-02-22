# KeyAuthConsumer

The Consumer to which this Key is associated. A Consumer can have many Key-auth credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from kong_admin_client.models.key_auth_consumer import KeyAuthConsumer

# TODO update the JSON string below
json = "{}"
# create an instance of KeyAuthConsumer from a JSON string
key_auth_consumer_instance = KeyAuthConsumer.from_json(json)
# print the JSON string representation of the object
print KeyAuthConsumer.to_json()

# convert the object into a dict
key_auth_consumer_dict = key_auth_consumer_instance.to_dict()
# create an instance of KeyAuthConsumer from a dict
key_auth_consumer_form_dict = key_auth_consumer.from_dict(key_auth_consumer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


