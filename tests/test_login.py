import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
from data import *
from helpers import *



class TestLogin:

    # 1 вход по кнопке «Войти в аккаунт» на главной
    def test_login_with_login_button(self, driver):
        driver.find_element(*Locators.enter_acc).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.order_button))
        check_button = driver.find_element(*Locators.order_button).text
        assert check_button == 'Оформить заказ'

    # 2 вход через кнопку «Личный кабинет»
    def test_login_with_lkbutton(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.order_button))
        check_button = driver.find_element(*Locators.order_button).text
        assert check_button == 'Оформить заказ'

    # 3 вход через кнопку в форме регистрации
    def test_login_registration_form(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.registrate_button).click()
        driver.find_element(*Locators.enter_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.enter_text_enter))
        driver.find_element(*Locators.enter_text_enter).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(Locators.order_button))
        check_button = driver.find_element(*Locators.order_butt).text
        assert check_button == 'Оформить заказ'

    # 4 вход через кнопку в форме восстановления пароля
    def test_login_restore_password_form(self, driver):
        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.recover_password).click()
        driver.find_element(*Locators.enter_button).click()
        driver.find_element(*Locators.email).send_keys(email)
        driver.find_element(*Locators.password).send_keys(password)
        driver.find_element(*Locators.enter_text_enter).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.order_button))
        check_button = driver.find_element(*Locators.order_button).text
        assert check_button == 'Оформить заказ'
