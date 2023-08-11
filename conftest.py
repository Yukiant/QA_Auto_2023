import pytest
from modules.api.clients.github import GitHub
from modules.ui.page_objects.ML_Tool_page_indiv import MLToolPage


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Yuliia"
        self.second_name = "Kosminska"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    """Fixture definition for lecture work - to see how fixtures are involved"""
    user = User()
    user.create()
    yield user
    user.remove()


@pytest.fixture
def github_api():
    """Fixture definition for lecture work - to test GitHub API"""
    api = GitHub()
    yield api


@pytest.fixture(scope="module")
def open_MLToolPage():
    """Fixture definition for individual homework - to run ui tests in one browser session"""
    page = MLToolPage()
    page.go_to()
    yield page
    page.close()
