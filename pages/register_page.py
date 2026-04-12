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
    VISIBLE_ERRORS = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/span[2]/span')

class RegistrationPage(BasePage):
    def choose_gender(self, gender):
        if gender.lower() == "male":
            self.click(Locators.MALE_RADIO)
        elif gender.lower() == "female":
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

    def get_visible_errors(self):
        errors_webelements = self.driver.find_elements(*Locators.VISIBLE_ERRORS)
        visible_errors = []
        for error in errors_webelements:
            visible_errors.append(error.text)
        return visible_errors