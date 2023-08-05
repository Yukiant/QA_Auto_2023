import requests

class GitHub:

    def get_user(self, username):
        r = requests.get(f'http://api.github.com/users/{username}')
        body = r.json()
        return body
    
    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories", params = {"q": name})
        body = r.json()
        return body

    # Below there are changes in this client done within the individual homework

    # Get all contributor commit activity
    def get_total_commits(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/stats/contributors')
        body = r.json()
        status = r.status_code
        return [status, body]

    # List repository languages
    def get_repo_languages(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/languages')
        body = r.json()
        return body