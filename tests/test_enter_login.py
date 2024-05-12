from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from data import TestUrls, TestUser
from locators import TestLocators


class TestEnterLogin:
    # тест доступности Главной страницы с указанными элементами
    def test_access_main_page(self, driver_chrome):
        driver_chrome.get(TestUrls.MAIN_PAGE_URL)
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_ACCOUNT))
        assert driver_chrome.current_url == TestUrls.MAIN_PAGE_URL

    # Вход - Проверь:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_enter_by_button_login_account_on_main_page(self, driver_chrome):
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_LOGIN_ACCOUNT))
        driver_chrome.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION)
                                    and EC.visibility_of_element_located(TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION))

        assert driver_chrome.current_url == TestUrls.LOGIN_PAGE_URL

        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION).send_keys(TestUser.email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION).send_keys(TestUser.password)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_AUTHORIZATION).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))

        assert driver_chrome.current_url == TestUrls.MAIN_PAGE_URL and driver_chrome.find_element(*TestLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ'

    # вход через кнопку «Личный кабинет»
    def test_enter_by_button_personal_account_on_main_page(self, driver_chrome):
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_PERSONAL_ACCOUNT))
        driver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION)
                                    and EC.visibility_of_element_located(TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION))

        assert driver_chrome.current_url == TestUrls.LOGIN_PAGE_URL

        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION).send_keys(TestUser.email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION).send_keys(TestUser.password)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_AUTHORIZATION).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))

        assert driver_chrome.current_url == TestUrls.MAIN_PAGE_URL and driver_chrome.find_element(
            *TestLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ'


# вход через кнопку в форме регистрации,
    def test_enter_by_button_enter_on_register_page(self, driver_chrome):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_ENTER_FOR_REGISTER))
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_REGISTER).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION)
                                    and EC.visibility_of_element_located(TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION))

        assert driver_chrome.current_url == TestUrls.LOGIN_PAGE_URL

        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION).send_keys(TestUser.email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION).send_keys(TestUser.password)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_AUTHORIZATION).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))

        assert driver_chrome.current_url == TestUrls.MAIN_PAGE_URL and driver_chrome.find_element(
            *TestLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ'

# вход через кнопку в форме восстановления пароля.
    def test_enter_by_button_enter_on_restore_page(self, driver_chrome):
        driver_chrome.get(TestUrls.RESTORE_PAGE_URL)
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_ENTER_FOR_RESTORE))
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_RESTORE).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION)
                                    and EC.visibility_of_element_located(TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION))

        assert driver_chrome.current_url == TestUrls.LOGIN_PAGE_URL

        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION).send_keys(TestUser.email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION).send_keys(TestUser.password)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_AUTHORIZATION).click()
        WDW(driver_chrome, 5).until(EC.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER))

        assert driver_chrome.current_url == TestUrls.MAIN_PAGE_URL and driver_chrome.find_element(
            *TestLocators.BUTTON_MAKE_ORDER).text == 'Оформить заказ'
