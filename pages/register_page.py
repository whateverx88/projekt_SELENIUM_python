from selenium.webdriver.common.by import By
from projekt_SELENIUM_python.pages.base_page import BasePage

class Locators:
    MALE_RADIO = (By.ID, "gender-male")
    FEMALE_RADIO = (By.ID, "gender-female")
    FIRST_NAME = (By.ID, "LastName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

class RegistrationPage(BasePage):
    def choose_gender(self, gender):
        if gender == "male":
            self.click(Locators.MALE_RADIO)
        elif gender == "female":
            self.click(Locators.FEMALE_RADIO)

    def enter_first_name(self):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys("John")

    def enter_last_name(self):
        self.driver.find_element(*Locators.LAST_NAME).send_keys("Smith")

    def enter_email(self):
        self.driver.find_element(*Locators.EMAIL).send_keys("test@test.pl")

    def enter_password(self):
        self.driver.find_element(*Locators.PASSWORD).send_keys("123qazxsw")

    def enter_confirm_password(self):
        self.driver.find_element(*Locators.CONFIRM_PASSWORD).send_keys("123qazxsw")

    def click_register_button(self):
        self.driver.find_element(*Locators.REGISTER_BUTTON).click()