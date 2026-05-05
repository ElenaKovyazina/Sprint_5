from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import generate_random_data_for_success_registration, generate_random_data_for_bad_registration


class TestStellarBurgersRegistration:

# Успешная регистрация на сайте

    def test_successfull_registration_in_personal_account(self, driver):

        name, email, password = generate_random_data_for_success_registration()

        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_NAME))
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        order_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'

# Ошибка регистрации на сайте при вводе пароля меньше 6 символов

    def test_unsuccessfull_registration_in_personal_account(self, driver):
        
        name, email, password = generate_random_data_for_bad_registration()

        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_LINK))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_NAME))
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REG_MESSAGE))

        assert error.text == 'Некорректный пароль'




