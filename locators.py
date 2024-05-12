from selenium.webdriver.common.by import By
class TestLocators:
    # Главная страница
    BUTTON_LOGIN_ACCOUNT = By.XPATH, "//button[text()='Войти в аккаунт']"
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"

    # Кнопка "Оформить заказ" на Главной странице после авторизации
    BUTTON_MAKE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"

    # Вкладки Конструктора "Булки" "Соусы" "Начинки"
    CONSTRUCTOR_TAB_BUNS = By.XPATH, "//div[.='Булки']"
    CONSTRUCTOR_TAB_SAUSES = By.XPATH, "//div[.='Соусы']"
    CONSTRUCTOR_TAB_FILLINGS = By.XPATH, "//div[.='Начинки']"

    # страница Авторизации зарегистрированного пользователя
    ## Поле "Email" на странице Авторизации
    FIELD_INPUT_NAME_FOR_AUTHORIZATION = By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
    ## Поле "Пароль" на странице Авторизации
    FIELD_INPUT_PASSWORD_FOR_AUTHORIZATION = By.XPATH, ".//label[text()='Пароль']//parent::*/input[@type='password' and @name='Пароль']"
    ## Кнопка "Войти" на странице Авторизации
    BUTTON_ENTER_FOR_AUTHORIZATION = By.XPATH, "//button[text()='Войти']"

    # страница Регистрации
    ## Кнопка "Войти" на странице Регистрации
    BUTTON_ENTER_FOR_REGISTER = By.XPATH, ".//p[text()='Уже зарегистрированы?']//parent::*//a[@href='/login' and text()='Войти']"

    # поле ввода Имени на странице Регистрация
    FIELD_INPUT_NAME_FOR_REGISTER = By.XPATH, ".//label[text()='Имя']//parent::*//input[@type='text' and @name='name']"
    # поле ввода Email на странице Регистрация
    FIELD_INPUT_EMAIL_FOR_REGISTER = By.XPATH, ".//label[text()='Email']//parent::*//input[@type='text' and @name='name']"
    # поле ввода Password на странице Регистрация
    FIELD_INPUT_PASSWORD_FOR_REGISTER = By.XPATH, ".//label[text()='Пароль']//parent::*//input[@type='password' and @name='Пароль']"

    ## кнопка Зарегистрироваться на странице Регистрация
    BUTTON_REGISTER_FOR_REGISTER = By.XPATH, ".//button[text()='Зарегистрироваться']"

    ## Сообщение об ошибке "Некорректный пароль" при неверном пароле на странице Регистрации
    MESSAGE_INCORRECT_PASSWORD = By.XPATH, ".//div[@class='input__container']/p[text()='Некорректный пароль']"

    # страница Восстановления
    ## Кнопка "Войти" на странице Восстановления
    BUTTON_ENTER_FOR_RESTORE = By.XPATH, ".//p[text()='Вспомнили пароль?']//parent::*//a[@href='/login' and text()='Войти']"

    # страница Личный Кабинет
    ## поле отображающее Имя зарегистрированного пользователя на странице Личный Кабинет
    FIELD_VIEW_NAME_FOR_PERSONAL_ACCOUNT = By.XPATH, ".//input[@type='text' and @name='Name']"
    ## поле отображающее Логин\Email зарегистрированного пользователя на странице Личный Кабинет
    FIELD_VIEW_EMAIL_FOR_PERSONAL_ACCOUNT = By.XPATH, ".//label[text()='Логин']/parent::*//input[@type='text' and @name='name']"

    ## Раздел "Профиль" в Личном Кабинете
    CURRENT_USER_PROFILE = By.CSS_SELECTOR, "Account_link__2ETsJ"
    ## Кнопка для перехода в Конструктор
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[text()='Конструктор']"
    ## Логотип STELLARS@BURGERS
    LOGOTYPE_STELLARSBURGERS = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"

    ## Кнопка Выхода из Профиля пользователя
    BUTTON_LOGOUT_ACCOUNT = By.XPATH, "//button[@type='button' and text()='Выход']"

