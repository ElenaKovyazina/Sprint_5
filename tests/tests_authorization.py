
from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersLogin:

  # Вход по кнопке «Войти в аккаунт» на главной
    def test_enter_login_main_button(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.LOGIN_MAIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('elena_suslova_44@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Alena2022)')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку «Личный кабинет»
    def test_enter_personal_account_button(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('elena_suslova_44@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Alena2022)')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку в форме регистрации
    def test_button_enter_login_page(self, driver):

        driver.get("https://stellarburgers.education-services.ru/register")
        
        driver.find_element(*Locators.REGISTRATION_LOGIN_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('elena_suslova_44@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Alena2022)')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'


    # Вход через кнопку в форме восстановления пароля
    def test_button_enter_password_recovery(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LOGIN_LINK).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_LOGIN).click()
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('elena_suslova_44@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Alena2022)')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'
