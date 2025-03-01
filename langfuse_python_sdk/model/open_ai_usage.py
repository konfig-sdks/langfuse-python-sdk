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


class OpenAIUsage(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Usage interface of OpenAI for improved compatibility.
    """


    class MetaOapg:
        
        class properties:
            
            
            class promptTokens(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'promptTokens':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class completionTokens(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'completionTokens':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class totalTokens(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'totalTokens':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "promptTokens": promptTokens,
                "completionTokens": completionTokens,
                "totalTokens": totalTokens,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["promptTokens"]) -> MetaOapg.properties.promptTokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completionTokens"]) -> MetaOapg.properties.completionTokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalTokens"]) -> MetaOapg.properties.totalTokens: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["promptTokens", "completionTokens", "totalTokens", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["promptTokens"]) -> typing.Union[MetaOapg.properties.promptTokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completionTokens"]) -> typing.Union[MetaOapg.properties.completionTokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalTokens"]) -> typing.Union[MetaOapg.properties.totalTokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["promptTokens", "completionTokens", "totalTokens", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        promptTokens: typing.Union[MetaOapg.properties.promptTokens, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        completionTokens: typing.Union[MetaOapg.properties.completionTokens, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        totalTokens: typing.Union[MetaOapg.properties.totalTokens, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OpenAIUsage':
        return super().__new__(
            cls,
            *args,
            promptTokens=promptTokens,
            completionTokens=completionTokens,
            totalTokens=totalTokens,
            _configuration=_configuration,
            **kwargs,
        )
