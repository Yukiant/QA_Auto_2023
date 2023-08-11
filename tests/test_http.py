import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("http://api.github.com/zen")
    print(f"Response is {r.text}")


@pytest.mark.http
def test_second_request():
    r = requests.get("http://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers

    assert body["name"] == "Chris Wanstrath"  # print(f'Response Body is {r.json()}')
    assert r.status_code == 200  # print(f'Response Status Code is {r.status_code}')
    assert (
        headers["Server"] == "GitHub.com"
    )  # print(f'Response Headers are {r.headers}')


@pytest.mark.http
def test_status_code_request():
    r = requests.get("http://api.github.com/users/sergii_butenko")
    assert r.status_code == 404
