from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.safari.options import Options
import time
import requests
import shutil

class MLToolPage(BasePage):
    URL = 'https://nanohub.org/resources/mseml'

    # class constructor
    def __init__(self) -> None:
        super().__init__()

    # the method opens the URL in the browser
    def go_to(self):
        self.driver.maximize_window()
        self.driver.get(MLToolPage.URL)
    
    # the method navigates to a previous browser page
    def go_back(self):
        self.driver.back()
        time.sleep(3)

    # the method checks page title
    def check_title(self, expected_title):
        return self.driver.title == expected_title

    # the method tries to launch the tool by clicking Launch button
    def launchTool(self):
        launch_button = self.driver.find_element(By.ID, "primary-document")
        launch_button.click()
        time.sleep(3)
    
    # the method returns current version of the tool
    def get_version(self):
        t = self.driver.find_element(By.CLASS_NAME, "curversion").text
        return float(t.split()[1])

    # the method navigates to Supporting docs subtab
    def go_supporting_docs(self):
        self.driver.find_element(By.XPATH, '//*[@id="sm-8"]/a/span').click()
        time.sleep(2)
        

    # The method finds a link to the downloadable document file and saves the renamed file to the project folder
    def download_resource(self, resource_name, new_file_name):
        time.sleep(2)
        link_elem = self.driver.find_element(By.PARTIAL_LINK_TEXT, resource_name)
        fullpath = link_elem.get_attribute('href')
        filereq = requests.get(fullpath, stream = True)
        with open(f"{new_file_name}.pdf","wb") as receive:
            shutil.copyfileobj(filereq.raw,receive)
        

    
    






        




    

