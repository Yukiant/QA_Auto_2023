from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomeNanohubPage(BasePage):
    URL = "https://nanohub.org"

    def __init__(self) -> None:
        """Class constructor"""
        super().__init__()

    def choose_from_submenu(self, submenu, submenuItem):
        """The method opens submenu under a top menu and chooses a submenu item"""
        # hover mouse pointer over a submenu
        a = ActionChains(self.driver)
        m = self.driver.find_element(By.PARTIAL_LINK_TEXT, submenu)
        a.move_to_element(m).perform()

        # wait until submenu items are displayed
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, submenuItem))
        )

        # click on a submenu item
        n = self.driver.find_element(By.PARTIAL_LINK_TEXT, submenuItem)
        a.move_to_element(n).click().perform()

        # wait until next page is loaded (actually its title is accessible)
        wait.until(
            EC.any_of(
                EC.title_contains(f"{submenu}"), EC.title_contains(f"{submenuItem}")
            )
        )

    def check_title(self, expected_title):
        """The method checks page title"""
        return self.driver.title == expected_title
