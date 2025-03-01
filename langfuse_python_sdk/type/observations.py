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

from langfuse_python_sdk.type.observation import Observation
from langfuse_python_sdk.type.utils_meta_response import UtilsMetaResponse

class RequiredObservations(TypedDict):
    data: typing.List[Observation]

    meta: UtilsMetaResponse

class OptionalObservations(TypedDict, total=False):
    pass

class Observations(RequiredObservations, OptionalObservations):
    pass
