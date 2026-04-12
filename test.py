# Project done on Ubuntu virtual machine setup on MacOS + M1 chipset. Some differences might appear compared to standard Ubuntu + WindowsOS.

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Additional flags for VM + ARM (M1 MacOS) and DOCKER running
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    options=options
)

driver.set_page_load_timeout(30)
driver.get("https://demo.nopcommerce.com")
driver.maximize_window()
time.sleep(5)
driver.quit()