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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from kong_admin_client.models.upstream_healthchecks_active import UpstreamHealthchecksActive
from kong_admin_client.models.upstream_healthchecks_passive import UpstreamHealthchecksPassive
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UpstreamHealthchecks(BaseModel):
    """
    UpstreamHealthchecks
    """ # noqa: E501
    active: Optional[UpstreamHealthchecksActive] = None
    passive: Optional[UpstreamHealthchecksPassive] = None
    threshold: Optional[Union[StrictFloat, StrictInt]] = 0
    __properties: ClassVar[List[str]] = ["active", "passive", "threshold"]

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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UpstreamHealthchecks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of active
        if self.active:
            _dict['active'] = self.active.to_dict()
        # override the default output from pydantic by calling `to_dict()` of passive
        if self.passive:
            _dict['passive'] = self.passive.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UpstreamHealthchecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "active": UpstreamHealthchecksActive.from_dict(obj.get("active")) if obj.get("active") is not None else None,
            "passive": UpstreamHealthchecksPassive.from_dict(obj.get("passive")) if obj.get("passive") is not None else None,
            "threshold": obj.get("threshold") if obj.get("threshold") is not None else 0
        })
        return _obj

