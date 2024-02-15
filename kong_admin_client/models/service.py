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
from kong_admin_client.models.service_client_certificate import ServiceClientCertificate
from typing import Optional, Set
from typing_extensions import Self

class Service(BaseModel):
    """
    service entities are abstractions of upstream services. The main attribute of a service is its URL which can be set as a single string or by specifying the `protocol`, `host`, `port` and `path` individually.
    """ # noqa: E501
    ca_certificates: Optional[List[StrictStr]] = Field(default=None, description="Array of `CA Certificate` object UUIDs that are used to build the trust store while verifying upstream server's TLS certificate. If set to `null` when Nginx default is respected. If default CA list in Nginx are not specified and TLS verification is enabled, then handshake with upstream server will always fail (because no CA are trusted).")
    client_certificate: Optional[ServiceClientCertificate] = None
    connect_timeout: Optional[StrictInt] = Field(default=60000, description="The timeout in milliseconds for establishing a connection to the upstream server.")
    created_at: Optional[StrictInt] = Field(default=None, description="Unix epoch when the resource was created.")
    enabled: Optional[StrictBool] = Field(default=True, description="Whether the service is active. If set to `false`, the proxy behavior will be as if any routes attached to it do not exist (404).")
    host: Optional[StrictStr] = Field(default=None, description="The host of the upstream server. Note that the host value is case sensitive.")
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = Field(default=None, description="The service name.")
    path: Optional[StrictStr] = Field(default=None, description="The path to be used in requests to the upstream server.")
    port: Optional[StrictInt] = Field(default=80, description="The upstream server port.")
    protocol: Optional[StrictStr] = Field(default='http', description="The protocol used to communicate with the upstream.")
    read_timeout: Optional[StrictInt] = Field(default=60000, description="The timeout in milliseconds between two successive read operations for transmitting a request to the upstream server.")
    retries: Optional[StrictInt] = Field(default=5, description="The number of retries to execute upon failure to proxy.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An optional set of strings associated with the service for grouping and filtering.")
    tls_verify: Optional[StrictBool] = Field(default=None, description="Whether to enable verification of upstream server TLS certificate. If set to `null`, then the Nginx default is respected.")
    tls_verify_depth: Optional[StrictInt] = Field(default=None, description="Maximum depth of chain while verifying Upstream server's TLS certificate. If set to `null`, then the Nginx default is respected.'")
    updated_at: Optional[StrictInt] = Field(default=None, description="Unix epoch when the resource was last updated.")
    url: Optional[StrictStr] = Field(default=None, description="Helper field to set `protocol`, `host`, `port` and `path` using a URL. This field is write-only and is not returned in responses.")
    write_timeout: Optional[StrictInt] = Field(default=60000, description="The timeout in milliseconds between two successive write operations for transmitting a request to the upstream server.")
    __properties: ClassVar[List[str]] = ["ca_certificates", "client_certificate", "connect_timeout", "created_at", "enabled", "host", "id", "name", "path", "port", "protocol", "read_timeout", "retries", "tags", "tls_verify", "tls_verify_depth", "updated_at", "url", "write_timeout"]

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
        """Create an instance of Service from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_certificate
        if self.client_certificate:
            _dict['client_certificate'] = self.client_certificate.to_dict()
        # set to None if tls_verify (nullable) is None
        # and model_fields_set contains the field
        if self.tls_verify is None and "tls_verify" in self.model_fields_set:
            _dict['tls_verify'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ca_certificates": obj.get("ca_certificates"),
            "client_certificate": ServiceClientCertificate.from_dict(obj["client_certificate"]) if obj.get("client_certificate") is not None else None,
            "connect_timeout": obj.get("connect_timeout") if obj.get("connect_timeout") is not None else 60000,
            "created_at": obj.get("created_at"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "host": obj.get("host"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "port": obj.get("port") if obj.get("port") is not None else 80,
            "protocol": obj.get("protocol") if obj.get("protocol") is not None else 'http',
            "read_timeout": obj.get("read_timeout") if obj.get("read_timeout") is not None else 60000,
            "retries": obj.get("retries") if obj.get("retries") is not None else 5,
            "tags": obj.get("tags"),
            "tls_verify": obj.get("tls_verify"),
            "tls_verify_depth": obj.get("tls_verify_depth"),
            "updated_at": obj.get("updated_at"),
            "url": obj.get("url"),
            "write_timeout": obj.get("write_timeout") if obj.get("write_timeout") is not None else 60000
        })
        return _obj


