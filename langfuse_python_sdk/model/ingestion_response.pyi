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


class IngestionResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "successes",
            "errors",
        }
        
        class properties:
            
            
            class successes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IngestionSuccess']:
                        return IngestionSuccess
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['IngestionSuccess'], typing.List['IngestionSuccess']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'successes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IngestionSuccess':
                    return super().__getitem__(i)
            
            
            class errors(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IngestionError']:
                        return IngestionError
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['IngestionError'], typing.List['IngestionError']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errors':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'IngestionError':
                    return super().__getitem__(i)
            __annotations__ = {
                "successes": successes,
                "errors": errors,
            }
    
    successes: MetaOapg.properties.successes
    errors: MetaOapg.properties.errors
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["successes"]) -> MetaOapg.properties.successes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["successes", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["successes"]) -> MetaOapg.properties.successes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> MetaOapg.properties.errors: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["successes", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        successes: typing.Union[MetaOapg.properties.successes, list, tuple, ],
        errors: typing.Union[MetaOapg.properties.errors, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IngestionResponse':
        return super().__new__(
            cls,
            *args,
            successes=successes,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from langfuse_python_sdk.model.ingestion_error import IngestionError
from langfuse_python_sdk.model.ingestion_success import IngestionSuccess
