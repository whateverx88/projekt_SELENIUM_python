import time
from faker import Faker
from projekt_SELENIUM_python.main import BaseTest
from projekt_SELENIUM_python.pages.register_page import RegistrationPage


class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.register_page = RegistrationPage(self.driver)
        self.fake = Faker()
        self.email = self.fake.email()

    def test_no_fist_name(self):
        print("Starting Registration Test - No first name")
        self.home_page.click_register()
        self.register_page.choose_gender("female")
        self.register_page.enter_last_name()
        self.register_page.enter_email(self.email)
        self.register_page.enter_password()
        self.register_page.enter_confirm_password()
        self.register_page.click_register_button()
        visible_errors = self.register_page.get_visible_errors()
        expected_errors = ["First name is required."]
        self.assertCountEqual(expected_errors, visible_errors)
        print("Test passed: correct error message")
        time.sleep(3)

    def test_successful_registration(self):
        print("Starting Registration Test - Successful registration")
        self.home_page.click_register()
        self.register_page.choose_gender("female")
        self.register_page.enter_first_name()
        self.register_page.enter_last_name()
        self.register_page.enter_email(self.email)
        self.register_page.enter_password()
        self.register_page.enter_confirm_password()
        self.register_page.click_register_button()
        self.register_page.wait_for_page()
        self.assertIn("Your registration completed", self.driver.page_source)
        self.register_page.click_continue_button()
        print("Test passed: registration completed successfully")
        time.sleep(3)