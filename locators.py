from selenium.webdriver.common.by import By

class Locators:

    # Личный кабинет
    account_button = (By.XPATH, "/html/body/div/div/header/nav/a/p")

    # Кнопка "Зарегистрироваться"
    registrate_button = (By.XPATH, "/html/body/div/div/main/div/div/p[1]/a")  # Кнопка "Зарегистрироваться"

    # Войти в аккаунт
    enter_head = (By.XPATH, "/html/body/div/div/main/div/h2")

    enter_click = (By.XPATH, "/html/body/div/div/main/div/form/button")

    # Ошибка - неверный пароль
    wrong_password = (By.XPATH, '//p[contains(text(),"Некорректный пароль")]')

    # Имя
    name = (By.XPATH, "html/body/div/div/main/div/form/fieldset[1]/div/div/input")  # Имя

    # Email
    email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # Email

    # Пароль
    password = (By.XPATH, './/input[@name="Пароль"]')  # Пароль

    # Войти в аккаунт
    enter_account = (By.XPATH, './/button[contains(text(), "Войти в аккаунт"]')
    enter_acc = (By.XPATH, '/html/body/div/div/main/section[2]/div/button')

    enter_text_enter = (By.XPATH, './/button[contains(text(),"Войти")]')

    # Оформить заказ
    order_button = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx "
                              "button_button_size_large__G21Vg']")
    order_butt = (By.XPATH, '/html/body/div/div/main/section[2]/div/button')

    # Кнопка ВОЙТИ
    enter_button = (By.XPATH, ".//a[text()='Войти']")

    # Восстановить пароль
    recover_password = (By.XPATH, ".//a[text()='Восстановить пароль']")

    # Кнопка ВЫХОД
    exit_button = (By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button')

    # текст ВХОД
    enter_text = (By.XPATH, ".// h2[text() = 'Вход']")

    # В конструктор
    constructor = (By.XPATH, "//p[contains(text(),'Конструктор')]")

    # Логотип
    logo = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

    # Выйти из ЛК
    exit_button = (By.XPATH, "//button[contains(text(),'Выход')]")

    # Булки
    bread = (By.XPATH, "//span[text() = 'Булки']")
    bread_check = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/h2[1]')

    # Соусы
    sauce = (By.XPATH, "//span[text() = 'Соусы']")
    sause_check = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/h2[2]')

    # Начинки
    filling = (By.XPATH, "//span[text() = 'Начинки']")
    filling_check = (By.XPATH, '/html/body/div/div/main/section[1]/div[2]/h2[3]')

    # Активированная секция
    active_section = (By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

    # Проверка личного кабинета
    check_account_page = (
        By.XPATH, ".//p[contains(text(),'В этом разделе вы можете изменить свои персональные данные')]")
