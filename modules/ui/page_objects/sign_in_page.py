from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"
    login_elem_id = "login_field"
    pass_elem_id = "password"
    btn_elem_id = "commit"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, SignInPage.login_elem_id)
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, SignInPage.pass_elem_id)
        pass_elem.send_keys(password)
        btn_elem = self.driver.find_element(By.NAME, SignInPage.btn_elem_id)
        btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
