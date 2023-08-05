import pytest
from modules.api.clients.github import GitHub
from modules.ui.page_objects.ML_Tool_page_indiv import MLToolPage

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Yuliia'
        self.second_name = 'Kosminska'

    def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()
    yield api

# below is a fixture definition - to run ui tests in one browser session
@pytest.fixture(scope='module')
def open_MLToolPage():
    page = MLToolPage()
    page.go_to()
    yield page
    page.close()