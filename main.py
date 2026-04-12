# Project done on Ubuntu virtual machine setup on MacOS + M1 chipset. Some differences might appear compared to standard Ubuntu + WindowsOS.

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from projekt_SELENIUM_python.pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):

        # Additional flags for VM + ARM (M1 MacOS) and DOCKER running to keep the setup stable
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
        print("Opening web driver...")
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://demowebshop.tricentis.com/")
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        time.sleep(1)

    def tearDown(self):
        print("Closing web browser. Thank you.")
        self.driver.quit()