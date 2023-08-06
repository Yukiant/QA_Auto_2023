from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ToolsNanohubPage(BasePage):
    URL = 'https://nanohub.org/resources/tools'

    # class constructor
    def __init__(self) -> None:
        super().__init__()

    # the method opens the URL in the browser
    def go_to(self):
        self.driver.maximize_window()
        self.driver.get(ToolsNanohubPage.URL)

    # the method enters search data into the tool search field
    def find_ML_tool(self, search_item):
        search_field = self.driver.find_element(By.ID, "toolsSearch")
        search_field.send_keys(search_item)
        time.sleep(2)
        found_element = self.driver.find_element(By.PARTIAL_LINK_TEXT, search_item)
        found_element.click()
        time.sleep(2)

    # the method checks page title
    def check_title(self, expected_title):
        return self.driver.title == expected_title
        
    



    

