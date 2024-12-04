#!/usr/bin/env python3
"""
utils.access_nested_map function
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    test the access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b":2}}, ("a",), {"b":2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test the acess_nested method.
        Args:
        nested_map: A dictionary that may have nested dictionaries
        path (List, tuple, set): Keys to get to the required value in the
        nested dictionary
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a":1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping
            path: Sequence) -> None:
        """
        Test method raises error
        Args:
        nested_map (Dict): A dicionary that may have nested dictionaries
        path (List, tuple, set): Keys to get to the required value
