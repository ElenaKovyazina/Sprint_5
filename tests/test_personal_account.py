from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersAccount:

  # Переход по клику в Личный кабинет
    def test_click_to_personal_account(self, driver):

        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        log_button=WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
       
        assert log_button.text == 'Войти'