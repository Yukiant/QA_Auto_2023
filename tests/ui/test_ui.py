import pytest
from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    # Create an object instance to access the browser
    driver = webdriver.Safari(service=Service(r"/usr/bin/safaridriver"))

    # open web page
    driver.get("https://github.com/login")

    # find the field to enter username
    login_elem = driver.find_element(By.ID, "login_field")

    # enter wrong username or email
    login_elem.send_keys("strangeemail@mistake.com")

    # find element to enter password
    pass_elem = driver.find_element(By.ID, "password")

    # enter wrong password
    pass_elem.send_keys("smthwrong")

    # find button sign-in
    btn_elem = driver.find_element(By.NAME, "commit")

    # left click
    btn_elem.click()

    # check Tab Title
    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3)

    # close the browser
    driver.close()
