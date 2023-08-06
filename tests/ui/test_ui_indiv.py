from modules.ui.page_objects.home_NH_page_indiv import HomeNanohubPage
from modules.ui.page_objects.tools_NH_page_indiv import ToolsNanohubPage
from modules.ui.page_objects.ML_Tool_page_indiv import MLToolPage
import pytest
import os.path
#import time

# 1
@pytest.mark.nano
def test_check_navigate_to_about_us():
# check that it is possible to navigate from NanoHUB home page to About Us page through the top menu
    home_page = HomeNanohubPage()
    home_page.go_to()
    home_page.choose_from_submenu("About", "What is nanoHUB?")
    assert home_page.check_title("nanoHUB.org - About Us")
    home_page.close()

# 2
@pytest.mark.nano
def test_check_navigate_to_tools():
# check that it is possible to navigate from NanoHUB home page to Resources: Tools page through the top menu
    home_page = HomeNanohubPage()
    home_page.go_to()
    home_page.choose_from_submenu("Explore", "Tools")
    assert home_page.check_title("nanoHUB.org - Resources: Tools")
    home_page.close()

# 3
@pytest.mark.nano
# check that it is possible to navigate to a specific ML tool page using the tool search
def test_find_ML_tool():
    tools_page = ToolsNanohubPage()
    tools_page.go_to()
    tools_page.find_ML_tool("Machine Learning for Materials Science")
    assert tools_page.check_title("nanoHUB.org - Resources: Machine Learning for Materials Science: Part 1")
    tools_page.close()

# 4
@pytest.mark.nano
# check that current version of the Tool is not earlier than 1.4
def test_version(open_MLToolPage):
    assert open_MLToolPage.get_version() >= 1.4

# 5
@pytest.mark.nano
# check that supporting documentation for the tool can be downloaded
def test_supporting_doc(open_MLToolPage):
    resource_to_download = "DS_ML_for_MSE"
    rename_to = "supporting_doc"
    open_MLToolPage.go_supporting_docs()
    open_MLToolPage.download_resource(resource_to_download, rename_to)
    assert os.path.isfile(f"/Users/Yuliia/Desktop/QAAuto/QA_Auto_2023/{rename_to}.pdf") == True

# 6
@pytest.mark.nano
# check that click on the Launch Tool button without login redirects to a login page
def test_launch_ML_tool_not_possible(open_MLToolPage):
    open_MLToolPage.launchTool()
    assert open_MLToolPage.check_title("nanoHUB.org - Login")
    open_MLToolPage.go_back()







