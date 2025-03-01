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

from langfuse_python_sdk.type.daily_metrics_details import DailyMetricsDetails
from langfuse_python_sdk.type.utils_meta_response import UtilsMetaResponse

class RequiredDailyMetrics(TypedDict):
    # A list of daily metrics, only days with ingested data are included.
    data: typing.List[DailyMetricsDetails]

    meta: UtilsMetaResponse

class OptionalDailyMetrics(TypedDict, total=False):
    pass

class DailyMetrics(RequiredDailyMetrics, OptionalDailyMetrics):
    pass
