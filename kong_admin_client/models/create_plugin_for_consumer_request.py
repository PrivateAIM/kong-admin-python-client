# coding: utf-8

"""
    Kong Admin API

    OpenAPI 3.0 spec for Kong Gateway's open source Admin API.  You can know more about Kong Gateway at [docs.konghq.com](https://docs.konghq.com) .Give Kong a star at [Kong/kong](https://github.com/kong/kong) repository.

    The version of the OpenAPI document: 3.5.0
    Contact: docs@konghq.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from kong_admin_client.models.list_plugins_for_consumer200_response_ordering import ListPluginsForConsumer200ResponseOrdering
from typing import Optional, Set
from typing_extensions import Self

class CreatePluginForConsumerRequest(BaseModel):
    """
    CreatePluginForConsumerRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the Plugin that's going to be added. Currently, the Plugin must be installed in every Kong instance separately. ")
    route: Optional[StrictStr] = Field(default=None, description="If set, the plugin will only activate when receiving requests via the specified route. Leave unset for the plugin to activate regardless of the route being used. Default: `null`. With form-encoded, the notation is `route.id=<route id> or route.name=<route name>`. With JSON, use `\"route\":{\"id\":\"<route id>\"}` or `\"route\":{\"name\":\"<route name>\"}`. ")
    service: Optional[StrictStr] = Field(default=None, description="If set, the plugin will only activate when receiving requests via one of the routes belonging to the specified service. ")
    consumer: Optional[StrictStr] = Field(default=None, description="If set, the plugin will activate only for requests where the specified has been authenticated. (Note that some plugins can not be restricted to consumers this way.) ")
    instance_name: Optional[StrictStr] = Field(default=None, description="The Plugin instance name. ")
    config: Optional[Dict[str, Any]] = Field(default=None, description="The configuration properties for the Plugin")
    protocols: Optional[List[StrictStr]] = Field(default=None, description="A list of the request protocols that will trigger this plugin.")
    enabled: Optional[StrictBool] = Field(default=True, description="Whether the plugin is applied. Default: `true`. ")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An optional set of strings associated with the Plugin for grouping and filtering. ")
    ordering: Optional[ListPluginsForConsumer200ResponseOrdering] = None
    __properties: ClassVar[List[str]] = ["name", "route", "service", "consumer", "instance_name", "config", "protocols", "enabled", "tags", "ordering"]

    @field_validator('protocols')
    def protocols_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['http', 'grpc', 'grpcs', 'tls', 'tcp']):
                raise ValueError("each list item must be one of ('http', 'grpc', 'grpcs', 'tls', 'tcp')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreatePluginForConsumerRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ordering
        if self.ordering:
            _dict['ordering'] = self.ordering.to_dict()
        # set to None if route (nullable) is None
        # and model_fields_set contains the field
        if self.route is None and "route" in self.model_fields_set:
            _dict['route'] = None

        # set to None if service (nullable) is None
        # and model_fields_set contains the field
        if self.service is None and "service" in self.model_fields_set:
            _dict['service'] = None

        # set to None if consumer (nullable) is None
        # and model_fields_set contains the field
        if self.consumer is None and "consumer" in self.model_fields_set:
            _dict['consumer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePluginForConsumerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "route": obj.get("route"),
            "service": obj.get("service"),
            "consumer": obj.get("consumer"),
            "instance_name": obj.get("instance_name"),
            "config": obj.get("config"),
            "protocols": obj.get("protocols"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "tags": obj.get("tags"),
            "ordering": ListPluginsForConsumer200ResponseOrdering.from_dict(obj["ordering"]) if obj.get("ordering") is not None else None
        })
        return _obj


