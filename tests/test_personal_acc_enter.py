import time

from locators import Locators
from data import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccaunt:
    def test_enter_acc(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.check_account_page))
        check = driver.find_element(*Locators.check_account_page).text
        assert check == 'В этом разделе вы можете изменить свои персональные данные'

    def test_from_account_to_constructor(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.constructor).click()
        check = driver.find_element(*Locators.order_button).text
        assert check == 'Оформить заказ'

    def test_from_account_to_logo(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.logo).click()
        check = driver.find_element(*Locators.order_button).text
        assert check == 'Оформить заказ'