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


class Session(BaseModel):
    id: str = Field(alias='id')

    created_at: datetime = Field(alias='createdAt')

    project_id: str = Field(alias='projectId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
