# Project done on Ubuntu virtual machine setup on MacOS + M1 chipset. Some differences might appear compared to standard Ubuntu + WindowsOS.

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from projekt_SELENIUM_python.pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):

        # Additional flags for VM + ARM (M1 MacOS) and DOCKER running
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
        print("Opening WebDriver...")
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        time.sleep(1)

    def tearDown(self):
        print("Closing WebDriver. Thank you")
        self.driver.quit()