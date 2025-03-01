# coding: utf-8

"""
    langfuse

    ## Authentication  Authenticate with the API using Basic Auth, get API keys in the project settings:  - username: Langfuse Public Key - password: Langfuse Secret Key

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class ScoreBody(BaseModel):
    trace_id: str = Field(alias='traceId')

    name: str = Field(alias='name')

    value: typing.Union[int, float] = Field(alias='value')

    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    observation_id: typing.Optional[typing.Optional[str]] = Field(None, alias='observationId')

    comment: typing.Optional[typing.Optional[str]] = Field(None, alias='comment')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
