from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersLogo:

  # Переход по клику в логотип Stellar Burgers
    def test_click_to_logo_SB(self, driver):

      driver.get("https://stellarburgers.education-services.ru/login")
      driver.find_element(*Locators.BTN_LOGO_SB).click()
      log_button=WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_MAIN_BUTTON))
       
      assert log_button.text == 'Войти в аккаунт'
