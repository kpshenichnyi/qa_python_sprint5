from faker import Faker
import random

# Основные страницы проекта
class TestUrls:
    # Главная страница
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/'
    # Страница авторизации
    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'
    # Страница Личного кабинета
    PROFILE_PAGE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    # Страница регистрации
    REGISTER_PAGE_URL = 'https://stellarburgers.nomoreparties.site/register'
    # Страница восстановления пароля
    RESTORE_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'

# данные по зарегистрированному тестовому
class TestUser:
    name = "Konstantin"
    email = "kp_8_2024@ya.ru"
    password = "password#2024"
    # correct_login = email
    # correct_password = password
    # incorrect_login = correct_login
    # incorrect_password = password

class FakeUser:
    fake = Faker()
    fake_name = fake.first_name()
    fake_email = f'{fake_name.lower()}_qa8_{random.randint(10, 99)}@example.net'
    fake_password_correct = fake.password(length=6)

