import unittest

from github_api import get_repos, get_commits, get_repo_commit_counts


class TestGitHubApi(unittest.TestCase):

    def test_get_repos(self):
        repos = get_repos("richkempinski")
        repo_names = [repo["name"] for repo in repos]
        self.assertIn("hellogitworld", repo_names)


    def test_get_commits(self):
        commits = get_commits(
            "richkempinski",
            "hellogitworld"
        )

        self.assertGreater(len(commits), 0)


    def test_get_repo_commit_counts(self):
        results = get_repo_commit_counts("richkempinski")

        found_hello_repo = False
        for result in results:
            if result.startswith("Repo: hellogitworld Number of commits"
            ):
                found_hello_repo = True

        self.assertTrue(found_hello_repo)
if __name__ == "__main__":
    unittest.main()