from modules.ui.page_objects.home_NH_page_indiv import HomeNanohubPage
from modules.ui.page_objects.tools_NH_page_indiv import ToolsNanohubPage
from modules.ui.page_objects.ML_Tool_page_indiv import MLToolPage
import pytest
import os.path


# 1
@pytest.mark.nano
def test_check_navigate_to_about_us():
    """check that it is possible to navigate from NanoHUB home page to About Us page through the top menu"""
    submenu = "About"
    submenuItem = "What is nanoHUB?"
    expected_title = "nanoHUB.org - About Us"

    home_page = HomeNanohubPage()
    home_page.go_to()
    home_page.choose_from_submenu(submenu, submenuItem)
    assert home_page.check_title(expected_title)
    home_page.close()


# 2
@pytest.mark.nano
def test_check_navigate_to_tools():
    """check that it is possible to navigate from NanoHUB home page to Resources: Tools page through the top menu"""
    submenu = "Explore"
    submenuItem = "Tools"
    expected_title = "nanoHUB.org - Resources: Tools"

    home_page = HomeNanohubPage()
    home_page.go_to()
    home_page.choose_from_submenu(submenu, submenuItem)
    assert home_page.check_title(expected_title)
    home_page.close()


# 3
@pytest.mark.nano
def test_find_ML_tool():
    """check that it is possible to navigate to a specific ML tool page using the tool search"""
    tool_to_navigate = "Machine Learning for Materials Science"
    expected_title = (
        "nanoHUB.org - Resources: Machine Learning for Materials Science: Part 1"
    )

    tools_page = ToolsNanohubPage()
    tools_page.go_to()
    tools_page.find_ML_tool(tool_to_navigate)
    assert tools_page.check_title(expected_title)
    tools_page.close()


# 4
@pytest.mark.nano
def test_version(open_MLToolPage):
    """check that current version of the Tool is not earlier than any specified version, for exmaple, 1.4"""
    minimal_allowed_version = 1.4
    
    assert open_MLToolPage.get_version() >= minimal_allowed_version


# 5
@pytest.mark.nano
def test_supporting_doc(open_MLToolPage):
    """check that supporting documentation for the tool can be downloaded"""
    resource_to_download = "DS_ML_for_MSE"
    rename_to = "supporting_doc"
    path_to_download = "/Users/Yuliia/Desktop/QAAuto/QA_Auto_2023/"
    
    # Go to Supporting Docs subtab and click to download documentation in pdf
    open_MLToolPage.go_supporting_docs()
    open_MLToolPage.download_resource(resource_to_download, rename_to)
    assert (
        os.path.isfile(path_to_download + f"{rename_to}.pdf")
        == True
    )


# 6
@pytest.mark.nano
def test_launch_ML_tool_not_possible(open_MLToolPage):
    """check that click on the Launch Tool button without login redirects to a login page"""
    expected_title = "nanoHUB.org - Login"

    open_MLToolPage.launchTool()
    assert open_MLToolPage.check_title(expected_title)
    open_MLToolPage.go_back()
