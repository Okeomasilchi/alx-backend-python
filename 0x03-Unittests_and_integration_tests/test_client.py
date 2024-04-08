#!/usr/bin/env python3
"""
unit test for Client
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case class for testing the GithubOrgClient class.
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct
        value without making actual HTTP calls.
        """

        # Mocking the response
        mock_response = {
          "name": org_name,
          "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
          }
        mock_get_json.return_value = mock_response

        # Creating an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Calling the org method
        result = client.org

        # Asserting that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
          f"https://api.github.com/orgs/{org_name}"
          )

        # Asserting that the result is correct
        self.assertEqual(result, mock_response)


if __name__ == "__main__":
    unittest.main()
