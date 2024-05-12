import pytest
import random

from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from data import TestUrls, TestUser, FakeUser
from locators import TestLocators


# Тесты на Регистрацию пользователя
class TestRegistration:
    # Успешную регистрацию - все поля заполнены корректно
    def test_success_registration_with_correct_name_login_password(self, driver_chrome):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_REGISTER).send_keys(FakeUser.fake_name)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_EMAIL_FOR_REGISTER).send_keys(FakeUser.fake_email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_REGISTER).send_keys(FakeUser.fake_password_correct)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_FOR_REGISTER).click()
        WDW(driver_chrome, 5).until(EC.url_to_be(TestUrls.LOGIN_PAGE_URL))

        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_AUTHORIZATION).send_keys(FakeUser.fake_email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION).send_keys(FakeUser.fake_password_correct)
        driver_chrome.find_element(*TestLocators.BUTTON_ENTER_FOR_AUTHORIZATION).click()

        driver_chrome.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WDW(driver_chrome, 5).until(EC.url_to_be(TestUrls.PROFILE_PAGE_URL))

        test_current_name = driver_chrome.find_element(*TestLocators.FIELD_VIEW_NAME_FOR_PERSONAL_ACCOUNT).get_attribute('value')
        test_current_email = driver_chrome.find_element(*TestLocators.FIELD_VIEW_EMAIL_FOR_PERSONAL_ACCOUNT).get_attribute(
            'value')

        assert (driver_chrome.current_url == TestUrls.PROFILE_PAGE_URL and
                test_current_name == FakeUser.fake_name and test_current_email == FakeUser.fake_email)


    # Поле «Имя» должно быть не пустым;
    def test_not_success_registration_with_empty_name(self, driver_chrome):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_EMAIL_FOR_REGISTER).send_keys(FakeUser.fake_email)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_REGISTER).send_keys(FakeUser.fake_password_correct)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_FOR_REGISTER).click()

        assert driver_chrome.current_url == TestUrls.REGISTER_PAGE_URL


    # в поле Email введён email в формате логин @ домен: например, 123 @ ya.ru.
    def test_correct_value_login(self, driver_chrome):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_REGISTER).send_keys(FakeUser.fake_name)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_EMAIL_FOR_REGISTER).send_keys(FakeUser.fake_email)

        current_email_name = driver_chrome.find_element(*TestLocators.FIELD_INPUT_EMAIL_FOR_REGISTER).get_attribute('value')
        correct_email_domain = driver_chrome.find_element(*TestLocators.FIELD_INPUT_EMAIL_FOR_REGISTER).get_attribute('value')

        assert FakeUser.fake_name.lower() in current_email_name and '@example.net' in correct_email_domain

    # Тест не успешной регистрации при пустом пароле
    def test_not_success_registration_with_empty_password(self, driver_chrome):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_NAME_FOR_REGISTER).send_keys(FakeUser.fake_name)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_EMAIL_FOR_REGISTER).send_keys(FakeUser.fake_email)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_FOR_REGISTER).click()

        assert driver_chrome.current_url == TestUrls.REGISTER_PAGE_URL


    # Ошибку для некорректного пароля.
    @pytest.mark.parametrize('incorrect_password', ["1", "12345"])
    def test_error_message_for_password_less_than_6_characters(self, driver_chrome, incorrect_password):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_REGISTER).send_keys(incorrect_password)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_FOR_REGISTER).click()
        find_element = driver_chrome.find_element(*TestLocators.MESSAGE_INCORRECT_PASSWORD).is_enabled()
        find_element_text = driver_chrome.find_element(*TestLocators.MESSAGE_INCORRECT_PASSWORD).text

        assert find_element == True and find_element_text == "Некорректный пароль"

    # Минимальный пароль — шесть символов.
    @pytest.mark.parametrize('correct_password', ["123456"])
    def test_min_6_characters_for_password(self, driver_chrome, correct_password):
        driver_chrome.get(TestUrls.REGISTER_PAGE_URL)
        driver_chrome.find_element(*TestLocators.FIELD_INPUT_PASSWORD_FOR_REGISTER).send_keys(correct_password)
        driver_chrome.find_element(*TestLocators.BUTTON_REGISTER_FOR_REGISTER).click()
        try:
            find_element = driver_chrome.find_element(*TestLocators.MESSAGE_INCORRECT_PASSWORD)
        except Exception: find_element = False

        assert find_element == False
