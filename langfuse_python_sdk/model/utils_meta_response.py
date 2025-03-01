# coding: utf-8

"""
    langfuse

    ## Authentication  Authenticate with the API using Basic Auth, get API keys in the project settings:  - username: Langfuse Public Key - password: Langfuse Secret Key

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from langfuse_python_sdk import schemas  # noqa: F401


class UtilsMetaResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "totalItems",
            "limit",
            "totalPages",
            "page",
        }
        
        class properties:
            page = schemas.IntSchema
            limit = schemas.IntSchema
            totalItems = schemas.IntSchema
            totalPages = schemas.IntSchema
            __annotations__ = {
                "page": page,
                "limit": limit,
                "totalItems": totalItems,
                "totalPages": totalPages,
            }
    
    totalItems: MetaOapg.properties.totalItems
    limit: MetaOapg.properties.limit
    totalPages: MetaOapg.properties.totalPages
    page: MetaOapg.properties.page
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalItems"]) -> MetaOapg.properties.totalItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["page", "limit", "totalItems", "totalPages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalItems"]) -> MetaOapg.properties.totalItems: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalPages"]) -> MetaOapg.properties.totalPages: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["page", "limit", "totalItems", "totalPages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        totalItems: typing.Union[MetaOapg.properties.totalItems, decimal.Decimal, int, ],
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, ],
        totalPages: typing.Union[MetaOapg.properties.totalPages, decimal.Decimal, int, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UtilsMetaResponse':
        return super().__new__(
            cls,
            *args,
            totalItems=totalItems,
            limit=limit,
            totalPages=totalPages,
            page=page,
            _configuration=_configuration,
            **kwargs,
        )
