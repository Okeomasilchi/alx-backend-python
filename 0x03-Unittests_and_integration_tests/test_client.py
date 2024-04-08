#!/usr/bin/env python3
"""
unit test for Client
"""

import unittest
from unittest.mock import patch, PropertyMock
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
        mock_response = {
          "name": org_name,
          "repos_url": f"https://api.github.com/orgs/{org_name}/repos"
          }
        mock_get_json.return_value = mock_response
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
          f"https://api.github.com/orgs/{org_name}"
          )

        self.assertEqual(result, mock_response)

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the expected value
        based on the mocked payload.
        """
        mocked_payload = {
          "repos_url": "https://api.github.com/orgs/google/repos"
          }
        with patch.object(
          GithubOrgClient,
          'org',
          new_callable=PropertyMock(return_value=mocked_payload)
          ):
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(
              result, "https://api.github.com/orgs/google/repos"
              )


if __name__ == "__main__":
    unittest.main()
