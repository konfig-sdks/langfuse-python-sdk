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


class CreateDatasetRunItemRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "observationId",
            "runName",
            "datasetItemId",
        }
        
        class properties:
            runName = schemas.StrSchema
            datasetItemId = schemas.StrSchema
            observationId = schemas.StrSchema
            __annotations__ = {
                "runName": runName,
                "datasetItemId": datasetItemId,
                "observationId": observationId,
            }
    
    observationId: MetaOapg.properties.observationId
    runName: MetaOapg.properties.runName
    datasetItemId: MetaOapg.properties.datasetItemId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runName"]) -> MetaOapg.properties.runName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datasetItemId"]) -> MetaOapg.properties.datasetItemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["observationId"]) -> MetaOapg.properties.observationId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["runName", "datasetItemId", "observationId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runName"]) -> MetaOapg.properties.runName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datasetItemId"]) -> MetaOapg.properties.datasetItemId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["observationId"]) -> MetaOapg.properties.observationId: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["runName", "datasetItemId", "observationId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        observationId: typing.Union[MetaOapg.properties.observationId, str, ],
        runName: typing.Union[MetaOapg.properties.runName, str, ],
        datasetItemId: typing.Union[MetaOapg.properties.datasetItemId, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateDatasetRunItemRequest':
        return super().__new__(
            cls,
            *args,
            observationId=observationId,
            runName=runName,
            datasetItemId=datasetItemId,
            _configuration=_configuration,
            **kwargs,
        )
