import time
from projekt_SELENIUM_python.main import BaseTest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()

    def test_no_fist_name(self):
        print("Starting Registration Test.")
        self.home_page.click_register()
        time.sleep(3)
        pass