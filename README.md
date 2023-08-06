# QA_Auto_2023
This repository is my student work on lecture materials and homework for a course "QA Automation" at _https://courses.prometheus.org.ua/_

Work on lecture materials is in accordance with lecture instructions.

**Individual part** consists in the following:

1. UI testing of _https://nanohub.org/_ using **pytest** and **selenium**:
   - the tests are marked with the mark "**nano**" (all new marks are added to **pytest.ini**);
   - added page objects to **/modules/ui/page_objects/**: **home_NH_page_indiv.py, tools_NH_page_indiv.py, ML_Tool_page_indiv.py**;
   - added tests **/tests/ui/test_ui_indiv.py**. Tests #1-3 work in a separate browser session, tests #4-6 work in a single browser session.
     To allow single browser session, a new fixture is added to **conftest.py**.

2. GitHub API testing using **pytest** and **requests**:
   - the tests are marked with the mark "**apind**";
   - the tests are added to **/tests/api/test_github_api.py**;
   - api-client is updated with new methods in **/modules/api/clients/github.py**.

3. Database testing using **pytest** and **sqlite3**:
   - the tests are marked with the mark "**dbind**";
   - the tests are added to **/tests/database/test_database.py**;  
   - new methods are added to **/modules/common/database.py**.
