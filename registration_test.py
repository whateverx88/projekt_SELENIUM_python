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
        self.register_page.enter_last_name()
        time.sleep(3)
        pass