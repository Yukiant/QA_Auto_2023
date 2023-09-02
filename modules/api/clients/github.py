import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"http://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", params={"q": name})
        body = r.json()

        return body

    # Below there are changes in this client done within the individual homework

    def get_total_commits(self, owner, repo):
        """Get all contributor commit activity
        https://docs.github.com/en/rest/metrics/statistics?apiVersion=2022-11-28#get-all-contributor-commit-activity
        """
        url = f"https://api.github.com/repos/{owner}/{repo}/stats/contributors"
        headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}   # header_auth = {'Authorization': 'Bearer <YOUR-TOKEN>'}
        r = requests.get(url, headers = headers)
        body = r.json()
        status = r.status_code

        return (status, body)

    def get_repo_languages(self, owner, repo):
        """List repository languages
        https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-languages
        """
        url = f"https://api.github.com/repos/{owner}/{repo}/languages"
        headers = {'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28'}
        r = requests.get(url, headers = headers)
        body = r.json()

        return body
