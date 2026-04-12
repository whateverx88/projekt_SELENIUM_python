import time
from projekt_SELENIUM_python.main import BaseTest
from projekt_SELENIUM_python.pages.register_page import RegistrationPage


class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.register_page = RegistrationPage(self.driver)

    def test_no_fist_name(self):
        print("Starting Registration Test.")
        self.home_page.click_register()
        self.register_page.choose_gender("female")
        self.register_page.enter_last_name()
        self.register_page.enter_email()
        self.register_page.enter_password()
        self.register_page.enter_confirm_password()
        self.register_page.click_register_button()
        visible_errors = self.register_page.get_visible_errors()
        expected_errors = ["First name is required."]
        self.assertCountEqual(expected_errors, visible_errors)
        print("Test passed: correct error message")
        time.sleep(3)