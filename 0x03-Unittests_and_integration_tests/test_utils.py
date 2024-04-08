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
    @parameterized.expand([({}, ("a",), "a"), ({"a": 1}, ("a", "b"), "b")])
    def test_access_nested_map_exception(
      self,
      nested_map,
      path,
      expected_error
      ):
        """
        Test that a KeyError is raised when accessing a
        non-existing key in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{expected_error}'")


if __name__ == "__main__":
    unittest.main()
