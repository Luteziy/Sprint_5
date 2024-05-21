from locators import Locators
from data import *
from helpers import *



class Testregistration:
    def test_registration(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.registrate_button).click()
        driver.find_element(*Locators.name).send_keys(name)
        driver.find_element(*Locators.email).send_keys(generate_email())
        driver.find_element(*Locators.password).send_keys(generate_password())
        driver.find_element(*Locators.registrate_button).click()
        check = driver.find_element(*Locators.enter_head).text
        assert check == "Вход"

    def test_wrong_pass(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.registrate_button).click()
        driver.find_element(*Locators.name).send_keys(name)
        driver.find_element(*Locators.email).send_keys(generate_email())
        driver.find_element(*Locators.password).send_keys(incorrect_password)
        driver.find_element(*Locators.registrate_button).click()
        wrong_password = driver.find_element(*Locators.wrong_password).text
        assert wrong_password == 'Некорректный пароль'