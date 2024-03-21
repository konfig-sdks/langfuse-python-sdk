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

from langfuse_python_sdk.type.ingestion_event import IngestionEvent

class RequiredIngestionBatchRequest(TypedDict):
    batch: typing.List[IngestionEvent]

class OptionalIngestionBatchRequest(TypedDict, total=False):
    pass

class IngestionBatchRequest(RequiredIngestionBatchRequest, OptionalIngestionBatchRequest):
    pass
