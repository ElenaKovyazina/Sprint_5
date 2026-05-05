from locators import Locators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestConstructorTransitions:

    # Переход к разделу "Булки"
    def test_buns_transition(self, driver):

        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*Locators.BTN_SAUSES).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BTN_SAUSES, 'class', 'tab_tab_type_current'))
        driver.find_element(*Locators.BTN_BUNS).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BTN_BUNS, 'class', 'tab_tab_type_current')) 

        assert 'tab_tab_type_current' in driver.find_element(*Locators.BTN_BUNS).get_attribute('class')


    # Переход к разделу "Соусы"
    def test_sauses_transition(self, driver):

        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*Locators.BTN_SAUSES).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(Locators.BTN_SAUSES, 'class', 'tab_tab_type_current'))
        
        assert 'tab_tab_type_current' in driver.find_element(*Locators.BTN_SAUSES).get_attribute('class')

        

    # Переход к разделу "Начинки"
    def test_fillings_transition(self, driver):

        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*Locators.BTN_FILLINGS).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element_attribute(Locators.BTN_FILLINGS, 'class', 'tab_tab_type_current'))
        
        assert 'tab_tab_type_current' in driver.find_element(*Locators.BTN_FILLINGS).get_attribute('class')

        

  
  


