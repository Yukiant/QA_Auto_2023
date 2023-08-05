import pytest
from modules.api.clients.github import GitHub

@ pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 42
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('repo-not-exist-qwertyuiop')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


# Below there are tests created within the individual homework

@pytest.mark.api
def test_total_commits(github_api):
    # check that number of total commits to my course repository is more than zero
    owner = "Yukiant"
    repo = "QA_Auto_2023"
    r = github_api.get_total_commits(owner, repo)
    n = r[1][0]['total'] # total number of commits
    print(f"\nNumber of commits is {n}")
    assert r[0] == 200, 'Response does not have Status Code = 200'
    assert n > 0, 'Total number of commits is not more than zero'

@pytest.mark.api
def test_fields_presence(github_api):
    # check that in the response all necessary fields 'total', 'weeks', 'author' are present.
    owner = "Yukiant"
    repo = "QA_Auto_2023"
    r = github_api.get_total_commits(owner, repo)
    field_list = set(r[1][0].keys())
    assert {'total', 'weeks', 'author'} == field_list

@pytest.mark.api
def test_repo_languages(github_api):
    # check that Python is the only programming language used in my course repository
    owner = "Yukiant"
    repo = "QA_Auto_2023"
    r = github_api.get_repo_languages(owner, repo)
    assert len(r) == 1 and list(r.keys())[0] == "Python"

@pytest.mark.api
def test_no_java_in_repo(github_api):
    # check that Java is not used in my course repository
    owner = "Yukiant"
    repo = "QA_Auto_2023"
    r = github_api.get_repo_languages(owner, repo)
    assert "Java" not in list(r.keys())