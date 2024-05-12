import pytest
from locators import TestLocators

# класс с тестами переходов по вкладкам Конструктора
class TestConstructor:

    # Перейти на вкладку "Начинки"
    def test_transit_to_fillings_in_constructor(self, driver_chrome):
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_FILLINGS).click()
        assert 'tab_tab_type_current__2BEPc' in  driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_FILLINGS).get_attribute("class")

    # Перейти на вкладку "Соусы"
    def test_transit_to_sauses_in_constructor(self, driver_chrome):
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_SAUSES).click()
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_SAUSES).get_attribute("class")


    # Перейти с вкладку "Начинки" и вернуться на вкладку "Булки"
    def test_transit_to_buns_in_constructor(self, driver_chrome):
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_FILLINGS).click()
        driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_BUNS).click()
        assert 'tab_tab_type_current__2BEPc' in driver_chrome.find_element(*TestLocators.CONSTRUCTOR_TAB_BUNS).get_attribute("class")
