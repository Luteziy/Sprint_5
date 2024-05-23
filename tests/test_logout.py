import time

from locators import Locators
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogout:
    def test_logout_account(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.exit_button))
        driver.find_element(*Locators.exit_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.enter_text))
        check = driver.find_element(*Locators.enter_text).text
        assert check == 'Вход'
