from selenium.webdriver.common.by import By
from projekt_SELENIUM_python.pages.base_page import BasePage

class Locators:
    LAST_NAME = (By.ID, "LastName")

class RegistrationPage(BasePage):
    def enter_last_name(self):
        self.driver.find_element(*Locators.LAST_NAME).send_keys("Smith")