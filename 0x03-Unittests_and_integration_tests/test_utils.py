#!/usr/bin/env python3
"""
Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()