from locators import Locators


class TestConstructor:
    def test_constructor_to_bread(self, driver):
        driver.find_element(*Locators.filling).click()
        driver.find_element(*Locators.bread).click()
        check_text = driver.find_element(*Locators.bread_check).text
        check_active = driver.find_element(*Locators.active_section).text
        assert check_text == check_active

    def test_constructor_to_sauces(self, driver):
        driver.find_element(*Locators.filling).click()
        driver.find_element(*Locators.sauce).click()
        check_text = driver.find_element(*Locators.sause_check).text
        check_active = driver.find_element(*Locators.active_section).text
        assert check_text == check_active

    def test_constructor_to_filling(self, driver):
        driver.find_element(*Locators.sauce).click()
        driver.find_element(*Locators.filling).click()
        check_text = driver.find_element(*Locators.filling_check).text
        check_active = driver.find_element(*Locators.active_section).text
        assert check_text == check_active