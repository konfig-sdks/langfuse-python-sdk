# coding: utf-8

"""
    langfuse

    ## Authentication  Authenticate with the API using Basic Auth, get API keys in the project settings:  - username: Langfuse Public Key - password: Langfuse Secret Key

    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import langfuse_python_sdk
from langfuse_python_sdk.paths.api_public_dataset_items import post
from langfuse_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiPublicDatasetItems(ApiTestMixin, unittest.TestCase):
    """
    ApiPublicDatasetItems unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
