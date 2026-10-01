import requests

def get_repos(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    repos = response.json()
    return repos

def get_commits(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    commits = response.json()
    return commits

def get_repo_commit_counts(user_id):
    repos = get_repos(user_id)

    results = []

    for repo in repos:
        repo_name = repo["name"]

        commits = get_commits(user_id, repo_name)

        results.append(
            f"Repo: {repo_name} Number of commits: {len(commits)}"
        )

    return results


if __name__ == "__main__":
    user_id = input("Enter GitHub user ID: ")

    results = get_repo_commit_counts(user_id)

    for result in results:
        print(result)
