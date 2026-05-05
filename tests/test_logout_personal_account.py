from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersAccount:

  # Выход по кнопке "Выйти" в Личном Кабинете
    def test_logout_from_personal_account(self, driver):

        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.EMAIL_INPUT))
        
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('elena_suslova_44@yandex.ru')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('Alena2022)')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_EXIT))
        driver.find_element(*Locators.BTN_EXIT).click()

        log_out = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))

        assert log_out.text == 'Войти'