from xml.sax.xmlreader import Locator

from projekt_SELENIUM_python.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    REGISTRATION_LINK = (By.CLASS_NAME,"ico-register")

class HomePage(BasePage):
    def click_register(self):
        self.driver.find_element(*Locators.REGISTRATION_LINK).click()
        return