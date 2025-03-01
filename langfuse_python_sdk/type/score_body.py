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


class RequiredScoreBody(TypedDict):
    traceId: str

    name: str

    value: typing.Union[int, float]

class OptionalScoreBody(TypedDict, total=False):
    id: typing.Optional[str]

    observationId: typing.Optional[str]

    comment: typing.Optional[str]

class ScoreBody(RequiredScoreBody, OptionalScoreBody):
    pass
