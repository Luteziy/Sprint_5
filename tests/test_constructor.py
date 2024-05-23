from locators import Locators


class TestConstructor:
    def test_constructor_to_bread(self, driver):
        driver.find_element(*Locators.filling).click()
        driver.find_element(*Locators.bread).click()
        assert driver.find_element(*Locators.active_section).text == driver.find_element(*Locators.bread).text


    def test_constructor_to_sauces(self, driver):
        driver.find_element(*Locators.filling).click()
        driver.find_element(*Locators.sauce).click()
        assert driver.find_element(*Locators.active_section).text == driver.find_element(*Locators.sauce).text

    def test_constructor_to_filling(self, driver):
        driver.find_element(*Locators.sauce).click()
        driver.find_element(*Locators.filling).click()
        assert driver.find_element(*Locators.active_section).text == driver.find_element(*Locators.filling).text