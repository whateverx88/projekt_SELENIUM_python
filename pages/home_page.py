from projekt_SELENIUM_python.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    REGISTRATION_LINK = (By.CLASS_NAME,"ico-register")

class HomePage(BasePage):
    def click_register(self):
        self.click(Locators.REGISTRATION_LINK)
        return