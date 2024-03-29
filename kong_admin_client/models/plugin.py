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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kong_admin_client.models.plugin_consumer import PluginConsumer
from kong_admin_client.models.plugin_route import PluginRoute
from kong_admin_client.models.plugin_service import PluginService
from typing import Optional, Set
from typing_extensions import Self

class Plugin(BaseModel):
    """
    A Plugin entity represents a plugin configuration that will be executed during the HTTP request/response lifecycle.
    """ # noqa: E501
    config: Optional[Dict[str, Any]] = Field(default=None, description="The configuration properties for the Plugin which can be found on the plugins documentation page in the [Kong Hub](https://docs.konghq.com/hub/).")
    consumer: Optional[PluginConsumer] = None
    created_at: Optional[StrictInt] = Field(default=None, description="Unix epoch when the resource was created.")
    enabled: Optional[StrictBool] = Field(default=True, description="Whether the plugin is applied.")
    id: Optional[StrictStr] = None
    instance_name: Optional[StrictStr] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the Plugin thats going to be added. Currently, the Plugin must be installed in every Kong instance separately.")
    ordering: Optional[Dict[str, Any]] = None
    protocols: Optional[List[StrictStr]] = Field(default=None, description="A list of the request protocols that will trigger this plugin. The default value, as well as the possible values allowed on this field, may change depending on the plugin type. For example, plugins that only work in stream mode will only support `\"tcp\"` and `\"tls\"`.")
    route: Optional[PluginRoute] = None
    service: Optional[PluginService] = None
    tags: Optional[List[StrictStr]] = Field(default=None, description="An optional set of strings associated with the Plugin for grouping and filtering.")
    updated_at: Optional[StrictInt] = Field(default=None, description="Unix epoch when the resource was last updated.")
    __properties: ClassVar[List[str]] = ["config", "consumer", "created_at", "enabled", "id", "instance_name", "name", "ordering", "protocols", "route", "service", "tags", "updated_at"]

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
        """Create an instance of Plugin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of consumer
        if self.consumer:
            _dict['consumer'] = self.consumer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of route
        if self.route:
            _dict['route'] = self.route.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service
        if self.service:
            _dict['service'] = self.service.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Plugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": obj.get("config"),
            "consumer": PluginConsumer.from_dict(obj["consumer"]) if obj.get("consumer") is not None else None,
            "created_at": obj.get("created_at"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "id": obj.get("id"),
            "instance_name": obj.get("instance_name"),
            "name": obj.get("name"),
            "ordering": obj.get("ordering"),
            "protocols": obj.get("protocols"),
            "route": PluginRoute.from_dict(obj["route"]) if obj.get("route") is not None else None,
            "service": PluginService.from_dict(obj["service"]) if obj.get("service") is not None else None,
            "tags": obj.get("tags"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


