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

from langfuse_python_sdk.pydantic.trace import Trace
from langfuse_python_sdk.pydantic.utils_meta_response import UtilsMetaResponse

class Traces(BaseModel):
    data: typing.List[Trace] = Field(alias='data')

    meta: UtilsMetaResponse = Field(alias='meta')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
