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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from kong_admin_client.models.create_target_for_upstream_request_upstream import CreateTargetForUpstreamRequestUpstream
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CreateTargetForUpstreamRequest(BaseModel):
    """
    CreateTargetForUpstreamRequest
    """ # noqa: E501
    upstream: Optional[CreateTargetForUpstreamRequestUpstream] = None
    weight: Optional[Annotated[int, Field(le=65535, strict=True, ge=0)]] = Field(default=100, description="The weight this target gets within the upstream loadbalancer (`0`-`65535`). If the hostname resolves to an SRV record, the `weight` value will be overridden by the value from the DNS record.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An optional set of strings associated with the Target for grouping and filtering.")
    __properties: ClassVar[List[str]] = ["upstream", "weight", "tags"]

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
        """Create an instance of CreateTargetForUpstreamRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of upstream
        if self.upstream:
            _dict['upstream'] = self.upstream.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateTargetForUpstreamRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "upstream": CreateTargetForUpstreamRequestUpstream.from_dict(obj.get("upstream")) if obj.get("upstream") is not None else None,
            "weight": obj.get("weight") if obj.get("weight") is not None else 100,
            "tags": obj.get("tags")
        })
        return _obj

