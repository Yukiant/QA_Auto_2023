# QA_Auto_2023

## About
This repository is my student work on lecture materials and homework for a course "Automation Software Testing by GlobalLogic" at _https://courses.prometheus.org.ua/_

## Notes for the teacher
Work on lecture materials is in accordance with lecture instructions.

**Individual part** consists in the following:

1. UI testing of _https://nanohub.org/_ using **Pytest** and **Selenium**:
   - the tests are marked with "**nano**" (all new markers are added to **pytest.ini**);
   - added page objects to **/modules/ui/page_objects/**: **home_NH_page_indiv.py, tools_NH_page_indiv.py, ML_Tool_page_indiv.py**;
   - added tests **/tests/ui/test_ui_indiv.py**. Tests #1-3 work in a separate browser session, tests #4-6 work in a single browser session;
   - new fixtures are added to **conftest.py**, including one allowing single browser session.

2. GitHub API testing using **Pytest** and **Requests**:
   - the tests are marked with "**apind**";
   - the tests are added to **/tests/api/test_github_api.py**;
   - api-client is updated with new methods in **/modules/api/clients/github.py**.

3. Database testing using **Pytest** and **Sqlite3**:
   - the tests are marked with "**dbind**";
   - the tests are added to **/tests/database/test_database.py**;  
   - new methods are added to **/modules/common/database.py**.

## To run UI tests:
```
pytest -m nano
```

## To run API tests:
```
pytest -m apind
```

## To run database tests:
```
pytest -m dbind
```

## To run tests form lecture work:
```
pytest -m marker
```
where `marker` is one of the following:
* `change` - tests to check modifying a name of a user
* `check` - tests to check users name (testing fixtures itself)
* `http` - tests to check HTTP Protocol
* `api` - tests to check API
* `database` - tests to check database
* `ui` - ui-testing
