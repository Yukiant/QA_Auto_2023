from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.safari.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import shutil


class MLToolPage(BasePage):
    URL = "https://nanohub.org/resources/mseml"
    xpath_supporting_doc = '//*[@id="sm-8"]/a/span'
    title_if_launched = "MSE_Machine_Learning_Tutorials"
    launch_button_id = "primary-document"
    version_id = "curversion"

    def __init__(self) -> None:
        """Class constructor"""
        super().__init__()

    def go_back(self):
        """The method navigates to a previous browser page"""
        self.driver.back()

    def go_supporting_docs(self):
        """The method navigates to Supporting docs subtab"""
        # Click on the subtab title
        self.driver.find_element(By.XPATH, MLToolPage.xpath_supporting_doc).click()

        # wait until elements under the subtab are loaded
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "pdf")))

    def download_resource(self, resource_name, new_file_name):
        """The method finds a link to the downloadable document file and saves the renamed file to the project folder"""
        link_elem = self.driver.find_element(By.PARTIAL_LINK_TEXT, resource_name)
        fullpath = link_elem.get_attribute("href")
        try:
            filereq = requests.get(fullpath, stream=True)
            with open(f"{new_file_name}.pdf", "wb") as receive:
                shutil.copyfileobj(filereq.raw, receive)
        except:
            print("Downloading error!")
            return False
        else:
            print("Download Ok!")
            return True

    def launch_tool(self):
        """The method tries to launch the tool by clicking Launch button"""
        # click on Launch Tool button
        launch_button = self.driver.find_element(By.ID, MLToolPage.launch_button_id)
        launch_button.click()

        # Wait until next page is loaded: either Login page or Launched Tool
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.any_of(
                EC.title_contains("Login"),
                EC.title_contains(f"{MLToolPage.title_if_launched}"),
            )
        )

    def get_version(self):
        """The method returns current version of the tool"""
        t = self.driver.find_element(By.CLASS_NAME, MLToolPage.version_id).text

        return float(t.split()[1])

    def check_title(self, expected_title):
        """The method checks page title"""
        return self.driver.title == expected_title