from projekt_SELENIUM_python.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    REGISTRATION_LINK = (By.CLASS_NAME,"ico-register")
    LOGIN_LINK = (By.CLASS_NAME,"ico-login")
    ACCOUNT_EMAIL = (By.CLASS_NAME, "account")

class HomePage(BasePage):
    def click_register(self):
        self.click(Locators.REGISTRATION_LINK)
        return

    def click_login(self):
        self.click(Locators.LOGIN_LINK)
        return

    def get_logged_user_email(self):
        return self.find_visible(Locators.ACCOUNT_EMAIL).text