# qa_python_sprint5
# Проект по автоматизации тестирования космической бургерной: STELLA@BURRGERS

Фреймворк для автотестов - pytest
Запуск автотестов - pytest -v
ИспользуемыЙ браузер - Chrome 124.0.6367.202

Необходимые доп.пакеты:
pip install selenium
pip install pytest
pip install faker

## **Содержание**:

### **README.md**
Описание проекта

### **locators.py**
Описываются используемые в тестах локаторы

### **data.py**
Содержит ссылки с адресами страниц и данные зарегистрированного\генерируемых пользователей

### **conftest.py**
Содержит фикстуру, подключающую драйвер для взаимодействия с браузером Chrome

### **tests**
Папка с файлами тестов:
- ***test_enter_login.py*** - тесты с проверками Входа из разных мест
- *test_access_main_page* - тест доступности Главной страницы с указанными элементами
- *test_enter_by_button_login_account_on_main_page* - вход по кнопке «Войти в аккаунт» на главной
- *test_enter_by_button_personal_account_on_main_page* - вход через кнопку «Личный кабинет»
- *test_enter_by_button_enter_on_register_page* - вход через кнопку в форме регистрации
- *test_enter_by_button_enter_on_restore_page* - вход через кнопку в форме восстановления пароля

- ***test_registration.py*** - тесты с проверками Входа из разных мест
- *def test_success_registration_with_correct_name_login_password* - Успешную регистрацию - все поля заполнены корректно
- *def test_not_success_registration_with_empty_name* - Поле «Имя» должно быть не пустым
- *test_correct_value_login* - в поле Email введён email в формате логин @ домен: например, 123 @ ya.ru.
- *test_not_success_registration_with_empty_password* - Тест не успешной регистрации при пустом пароле
- *test_error_message_for_password_less_than_6_characters* - Ошибку для некорректного пароля
- *test_min_6_characters_for_password* - Минимальный пароль — шесть символов

- ***test_transition.py*** - тесты с проверками переходов
- *def test_transition_click_on_personal_account* - Тест перехода на страницу Профиля зарегистрированного пользователя
- *test_transition_click_on_constructor* - Тест перехода на страницу Конструктора из Профиля
- *test_transition_click_on_logotype_stellarsburgers* - Тест перехода по клику на логотип Stellars@Burgers
- *test_logout_from_personal_account* - Выход из Личного Кабинета

- ***test_constructor.py*** - тесты с проверками доступности вкладок конструктора
- *test_transit_to_fillings_in_constructor* - Перейти на вкладку "Начинки"
- *test_transit_to_sauses_in_constructor* - Перейти на вкладку "Соусы"
- *test_transit_to_buns_in_constructor* - Перейти с вкладку "Начинки" и вернуться на вкладку "Булки"