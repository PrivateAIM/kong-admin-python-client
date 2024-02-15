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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from kong_admin_client.models.get_sni_with_certificate200_response_data_inner_certificate import GetSniWithCertificate200ResponseDataInnerCertificate
from typing import Optional, Set
from typing_extensions import Self

class GetSniWithCertificate200ResponseDataInner(BaseModel):
    """
    GetSniWithCertificate200ResponseDataInner
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier or the name attribute of the Certificate whose SNIs are to be retrieved. When using this endpoint, only SNIs associated to the specified Certificate will be listed.")
    name: Optional[StrictStr] = Field(default=None, description="The SNI name to associate with the given certificate. ")
    created_at: Optional[StrictInt] = Field(default=None, description="Unix epoch when the resource was created. ")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An optional set of strings associated with the SNIs for grouping and filtering. ")
    certificate: Optional[GetSniWithCertificate200ResponseDataInnerCertificate] = None
    __properties: ClassVar[List[str]] = ["id", "name", "created_at", "tags", "certificate"]

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
        """Create an instance of GetSniWithCertificate200ResponseDataInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of certificate
        if self.certificate:
            _dict['certificate'] = self.certificate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSniWithCertificate200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created_at": obj.get("created_at"),
            "tags": obj.get("tags"),
            "certificate": GetSniWithCertificate200ResponseDataInnerCertificate.from_dict(obj["certificate"]) if obj.get("certificate") is not None else None
        })
        return _obj


