import pytest
from selenium import webdriver
from data import TestUrls


# фикстура с драйвером для Chrome и подключению\отключению к\от тестируемому(-ого) проекту(-а)
@pytest.fixture
def driver_chrome():
    driver_chrome = webdriver.Chrome()
    driver_chrome.maximize_window()
    driver_chrome.get(TestUrls.MAIN_PAGE_URL)

    yield driver_chrome

    driver_chrome.quit()
