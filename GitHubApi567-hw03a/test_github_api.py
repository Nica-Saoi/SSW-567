import unittest
from unittest.mock import patch, Mock

from github_api import get_repos, get_commits, get_repo_commit_counts


class TestGitHubApi(unittest.TestCase):

    @patch("github_api.requests.get")
    def test_get_repos(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

        mock_get.return_value = mock_response

        result = get_repos("testuser")

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Repo1")

    @patch("github_api.requests.get")
    def test_get_commits(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {"sha": "123"},
            {"sha": "456"}
        ]

        mock_get.return_value = mock_response

        result = get_commits("testuser", "Repo1")

        self.assertEqual(len(result), 2)

    @patch("github_api.get_commits")
    @patch("github_api.get_repos")
    def test_get_repo_commit_counts(
        self,
        mock_get_repos,
        mock_get_commits
    ):
        mock_get_repos.return_value = [
            {"name": "Repo1"},
            {"name": "Repo2"}
        ]

        mock_get_commits.side_effect = [
            [{"sha": "1"}, {"sha": "2"}],
            [{"sha": "3"}]
        ]

        result = get_repo_commit_counts("testuser")

        expected = [
            "Repo: Repo1 Number of commits: 2",
            "Repo: Repo2 Number of commits: 1"
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()