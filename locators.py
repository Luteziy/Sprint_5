from selenium.webdriver.common.by import By

class Locators:

    # Личный кабинет
    account_button = (By.XPATH, "//a[@href = '/account']")

    # Кнопка "Зарегистрироваться"
    registrate_button = (By.XPATH, "//a[@href = '/register']")  # Вы — новый пользователь? Кнопка "Зарегистрироваться"

    # Кнопка Загеристрироваться(сама кнопка)
    register = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Имя
    name = (By.XPATH, './/input[@name="name"]')  # Имя

    # Email
    email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Email

    # Пароль
    password = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")  # Пароль

    # Надпись "Вход"
    enter_text = (By.XPATH, ".// h2[text() = 'Вход']")
    #_____________________________________________

    # Войти в аккаунт
    enter_text_enter = (By.XPATH, './/button[contains(text(),"Войти")]')

    # Ошибка - неверный пароль
    wrong_password = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    # Проверка личного кабинета
    check_account_page = (
        By.XPATH, ".//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")

    # В конструктор
    constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Кнопка ВЫХОД
    exit_button = (By.XPATH, './/button[contains(text(),"Выход")]')

    # Войти в аккаунт
    enter_account = (By.XPATH, './/button[contains(text(), "Войти в аккаунт"]')

    # Логотип
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    # Оформить заказ
    order_button = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx "
                              "button_button_size_large__G21Vg']")

    # Кнопка ВОЙТИ
    enter_button = (By.XPATH, ".//a[text()='Войти']") # Уже зарегистрированы? Войти

    # Восстановить пароль
    recover_password = (By.XPATH, ".//a[text()='Восстановить пароль']")

    # Булки
    bread = (By.XPATH, "//span[text() = 'Булки']")

    # Соусы
    sauce = (By.XPATH, "//span[text() = 'Соусы']")

    # Начинки
    filling = (By.XPATH, "//span[text() = 'Начинки']")

    # Активированная секция
    active_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")