from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestStellarBurgersConsructor:

  # Переход по клику в Конструктор
    def test_click_to_constructor(self, driver):

      driver.get("https://stellarburgers.education-services.ru/login")
      
      driver.find_element(*Locators.BTN_CONSTRUCTOR).click()
      log_button=WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_MAIN_BUTTON))
       
      assert log_button.text == 'Войти в аккаунт'
