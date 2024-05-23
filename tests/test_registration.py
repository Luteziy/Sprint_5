from locators import Locators
from data import *
from helpers import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



class Testregistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.registrate_button).click()
        driver.find_element(*Locators.name).send_keys(name)
        driver.find_element(*Locators.email).send_keys(generate_email())
        driver.find_element(*Locators.password).send_keys(generate_password())
        driver.find_element(*Locators.register).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.enter_text))
        check = driver.find_element(*Locators.enter_text).text
        assert check == "Вход"

    def test_wrong_pass(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.registrate_button).click()
        driver.find_element(*Locators.name).send_keys(name)
        driver.find_element(*Locators.email).send_keys(generate_email())
        driver.find_element(*Locators.password).send_keys(incorrect_password)
        driver.find_element(*Locators.register).click()
        wrong_password = driver.find_element(*Locators.wrong_password).text
        assert wrong_password == 'Некорректный пароль'