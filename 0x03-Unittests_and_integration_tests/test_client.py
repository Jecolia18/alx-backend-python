#!/usr/bin/env python3
""" testing client module mod"""

import unittest
from typing import Dict
from unittest.mock import (
        MagicMock,
        Mock,
        PropertyMock,
        patch,
        )
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
        GithubOrgClient
        )
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(unittest, TestCase):
    """`Githuborgclient` class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login'}: "abc"}),
        ])
    @patch(
            "client.get_json",
            )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
