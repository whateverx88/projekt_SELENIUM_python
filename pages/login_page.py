from selenium.webdriver.common.by import By
from projekt_SELENIUM_python.pages.base_page import BasePage

class Locators:
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CLASS_NAME, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='validation-summary-errors']//li")

class LoginPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_visible(Locators.ERROR_MESSAGE).text