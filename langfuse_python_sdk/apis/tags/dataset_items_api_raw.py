# coding: utf-8

"""
    langfuse

    ## Authentication  Authenticate with the API using Basic Auth, get API keys in the project settings:  - username: Langfuse Public Key - password: Langfuse Secret Key

    Generated by: https://konfigthis.com
"""

from langfuse_python_sdk.paths.api_public_dataset_items.post import CreateRaw
from langfuse_python_sdk.paths.api_public_dataset_items_id.get import GetRaw


class DatasetItemsApiRaw(
    CreateRaw,
    GetRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
