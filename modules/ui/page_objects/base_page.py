from selenium import webdriver
from selenium.webdriver.safari.service import Service

class BasePage:
    PATH = r"/usr/bin/safaridriver"

    def __init__(self) -> None:
        self.driver = webdriver.Safari(service=Service(r"/usr/bin/safaridriver"))

    def close(self):
        self.driver.close()
