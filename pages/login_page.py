from selenium.webdriver.common.by import By
from projekt_SELENIUM_python.pages.base_page import BasePage

class Locators:
    EMAIL = (By.XPATH, '//*[@id="Email"]')
    PASSWORD = (By.XPATH, '//*[@id="Password"]')
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[1]")

class LoginPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element(*Locators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_visible(Locators.ERROR_MESSAGE).text