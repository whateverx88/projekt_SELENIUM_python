
from projekt_SELENIUM_python.main import BaseTest
from projekt_SELENIUM_python.pages.home_page import HomePage
from projekt_SELENIUM_python.pages.login_page import LoginPage
import time

class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver)

    def test_successful_login(self):
        print("Starting Login Test - using previously defined email and password")
        self.home_page.click_login()
        self.login_page.enter_email("test_ALK_TAS@test.pl")
        self.login_page.enter_password("123qazxsw")
        self.login_page.click_login_button()
        actual_email = self.home_page.get_logged_user_email()
        self.assertEqual("test_ALK_TAS@test.pl", actual_email)
        print("Test passed: login successful with",actual_email," user")
        time.sleep(3)

    def test_login_wrong_password(self):
        print("Starting Login Test - wrong password")
        self.home_page.click_login()
        self.login_page.enter_email("test_ALK_TAS@test.pl")
        self.login_page.enter_password("wrongpassword")
        self.login_page.click_login_button()
        error = self.login_page.get_error_message()
        self.assertIn("Login was unsuccessful. Please correct the errors and try again.", error)
        print("Test passed: error message displayed: ", error)