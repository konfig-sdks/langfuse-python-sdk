# coding: utf-8

"""
    langfuse

    ## Authentication  Authenticate with the API using Basic Auth, get API keys in the project settings:  - username: Langfuse Public Key - password: Langfuse Secret Key

    Generated by: https://konfigthis.com
"""

from langfuse_python_sdk.paths.api_public_dataset_run_items.post import Create
from langfuse_python_sdk.apis.tags.dataset_run_items_api_raw import DatasetRunItemsApiRaw


class DatasetRunItemsApi(
    Create,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DatasetRunItemsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DatasetRunItemsApiRaw(api_client)
