#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case class for testing the access_nested_map function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with different inputs.

        Args:
          nested_map (dict): The nested map to be accessed.
          path (tuple): The path to the desired value in the nested map.
          expected_result: The expected result of accessing the nested map.

        Returns:
          None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(
      self, nested_map, path, expected_error):
        """
        Test that a KeyError is raised when accessing a
        non-existing key in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{expected_error}'")


class TestGetJson(unittest.TestCase):
    """
    Test case class for testing the get_json function.
    """
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns the expected result
        without making actual HTTP calls.
        """

        # Mocking the response
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Calling the get_json function
        result = get_json(test_url)

        # Asserting that requests.get was called once
        # with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Asserting that the output of get_json is
        # equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
