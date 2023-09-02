from selenium import webdriver
from selenium.webdriver.safari.service import Service


class BasePage:
    PATH = r"/usr/bin/safaridriver"

    def __init__(self) -> None:
        self.driver = webdriver.Safari(service = Service(BasePage.PATH))

    def close(self):
        self.driver.close()

    def go_to(self, URL):
        """The method opens the URL in the browser"""
        self.driver.maximize_window()
        self.driver.get(URL)
