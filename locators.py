from selenium.webdriver.common.by import By

class Locators:

    # Главная страница
    LOGIN_MAIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text() = "Личный Кабинет"]')
    
    # Страница входа в персональный аккаунт
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    
    # Страница регистрации
    REG_NAME = (By.XPATH, "//input[@name='name']")
    REG_EMAIL = (By.XPATH, "//label[text()='Email']/../input")
    REG_PASSWORD = (By.XPATH, "//input[@type='password']") 
    REG_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REG_MESSAGE = (By.XPATH, ".//p[contains(@class, 'input__error')]")

    # Кнопки "Войти" в форме регистрации
    REGISTRATION_LOGIN_LINK = (By.XPATH, '//a[text() = "Войти"]')
    
    # Кнопка "Войти" в форме восстановление пароля
    FORGOT_PASSWORD_LOGIN = (By.XPATH, '//a[text() = "Войти"]')
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, '//a[text() = "Восстановить пароль"]')
      
    #Кнопка "Оформить заказ"
    BTN_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")

    #Кнопка "Конструктор"
    BTN_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]') 

    #Кнопка логотип Stellar Burgers
    BTN_LOGO_SB = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')

    #Кнопка "Выход" в Личном кабинете
    BTN_EXIT = (By.XPATH, ".//button[text()='Выход']")

    #Кнопка Булки
    BTN_BUNS = (By.XPATH, "//div[span[text()='Булки']]")

    #Кнопка Соусы
    BTN_SAUSES = (By.XPATH, "//div[span[text()='Соусы']]")

    #Кнопка Начинки
    BTN_FILLINGS = (By.XPATH, "//div[span[text()='Начинки']]")