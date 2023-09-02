from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ToolsNanohubPage(BasePage):
    URL = "https://nanohub.org/resources/tools"
    search_field_id = "toolsSearch"

    def __init__(self) -> None:
        """Class constructor"""
        super().__init__()

    def find_ML_tool(self, search_item):
        """The method enters search data into the tool search field"""
        # enter data into the search field
        search_field = self.driver.find_element(By.ID, ToolsNanohubPage.search_field_id)
        search_field.send_keys(search_item)

        # wait until search results are accessible or return message if a tool is not found
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, search_item))
            )
        except:
            return "Tool is not found"

        # Click on search results (active link)
        found_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, search_item)
        found_element.click()

        # wait until next page is loaded (actually its title is accessible)
        wait.until(EC.title_contains(f"{search_item}"))

    def check_title(self, expected_title):
        """The method checks page title"""
        return self.driver.title == expected_title
