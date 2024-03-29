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

from pydantic import BaseModel, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateUpstreamRequestHealthchecksPassiveUnhealthy(BaseModel):
    """
    CreateUpstreamRequestHealthchecksPassiveUnhealthy
    """ # noqa: E501
    http_statuses: Optional[List[StrictInt]] = Field(default=None, description="An array of HTTP statuses which represent unhealthiness when produced by proxied traffic, as observed by passive health checks. With form-encoded, the notation is `http_statuses[]=429&http_statuses[]=500`. With JSON, use an array.")
    timeouts: Optional[StrictInt] = Field(default=0, description="Number of timeouts in proxied traffic to consider a target unhealthy, as observed by passive health checks.")
    http_failures: Optional[StrictInt] = Field(default=0, description="Number of HTTP failures in proxied traffic (as defined by `healthchecks.passive.unhealthy.http_statuses`) to consider a target unhealthy, as observed by passive health checks.")
    tcp_failures: Optional[StrictInt] = Field(default=0, description="Number of TCP connection failures to consider a target unhealthy, as observed by passive health checks.")
    __properties: ClassVar[List[str]] = ["http_statuses", "timeouts", "http_failures", "tcp_failures"]

    @field_validator('http_statuses')
    def http_statuses_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set([429, 500, 503]):
                raise ValueError("each list item must be one of (429, 500, 503)")
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
        """Create an instance of CreateUpstreamRequestHealthchecksPassiveUnhealthy from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateUpstreamRequestHealthchecksPassiveUnhealthy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "http_statuses": obj.get("http_statuses"),
            "timeouts": obj.get("timeouts") if obj.get("timeouts") is not None else 0,
            "http_failures": obj.get("http_failures") if obj.get("http_failures") is not None else 0,
            "tcp_failures": obj.get("tcp_failures") if obj.get("tcp_failures") is not None else 0
        })
        return _obj


