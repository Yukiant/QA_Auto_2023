from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomeNanohubPage(BasePage):
    URL = 'https://nanohub.org'

    # class constructor
    def __init__(self) -> None:
        super().__init__()

    # the method opens the URL in the browser
    def go_to(self):
        self.driver.maximize_window()
        self.driver.get(HomeNanohubPage.URL)

    # the method checks page title
    def check_title(self, expected_title):
        return self.driver.title == expected_title
    
    # the method opens submenu under a top menu and chooses a submenu item
    def choose_from_submenu(self, submenu, submenuItem):
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.PARTIAL_LINK_TEXT, submenu)
        a.move_to_element(m).perform()
        time.sleep(1)
        n = self.driver.find_element(By.PARTIAL_LINK_TEXT, submenuItem)
        a.move_to_element(n).click().perform()
        time.sleep(2)



    

