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

    @patch('client.get_json')
    @patch(
      'client.GithubOrgClient._public_repos_url',
      new_callable=PropertyMock
      )
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """
        Test that public_repos returns the expected list
        of repositories based on a mocked payload.
        """
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "another-repo"},
        ]
        mock_get_json.return_value = test_payload
        mock_repos_url.return_value = "https://test.url/repos"
        client = GithubOrgClient("test-org")
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2", "another-repo"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
          "https://test.url/repos"
          )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test that has_license returns the expected value.
        """
        client = GithubOrgClient("example_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
