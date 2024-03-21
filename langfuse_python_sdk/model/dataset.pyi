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


class Dataset(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "createdAt",
            "name",
            "id",
            "items",
            "projectId",
            "runs",
            "updatedAt",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            projectId = schemas.StrSchema
            createdAt = schemas.DateTimeSchema
            updatedAt = schemas.DateTimeSchema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DatasetItem']:
                        return DatasetItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DatasetItem'], typing.List['DatasetItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DatasetItem':
                    return super().__getitem__(i)
        
            @staticmethod
            def runs() -> typing.Type['DatasetRuns']:
                return DatasetRuns
            __annotations__ = {
                "id": id,
                "name": name,
                "projectId": projectId,
                "createdAt": createdAt,
                "updatedAt": updatedAt,
                "items": items,
                "runs": runs,
            }
    
    createdAt: MetaOapg.properties.createdAt
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    items: MetaOapg.properties.items
    projectId: MetaOapg.properties.projectId
    runs: 'DatasetRuns'
    updatedAt: MetaOapg.properties.updatedAt
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["runs"]) -> 'DatasetRuns': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "projectId", "createdAt", "updatedAt", "items", "runs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updatedAt"]) -> MetaOapg.properties.updatedAt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["runs"]) -> 'DatasetRuns': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "projectId", "createdAt", "updatedAt", "items", "runs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        items: typing.Union[MetaOapg.properties.items, list, tuple, ],
        projectId: typing.Union[MetaOapg.properties.projectId, str, ],
        runs: 'DatasetRuns',
        updatedAt: typing.Union[MetaOapg.properties.updatedAt, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Dataset':
        return super().__new__(
            cls,
            *args,
            createdAt=createdAt,
            name=name,
            id=id,
            items=items,
            projectId=projectId,
            runs=runs,
            updatedAt=updatedAt,
            _configuration=_configuration,
            **kwargs,
        )

from langfuse_python_sdk.model.dataset_item import DatasetItem
from langfuse_python_sdk.model.dataset_runs import DatasetRuns
