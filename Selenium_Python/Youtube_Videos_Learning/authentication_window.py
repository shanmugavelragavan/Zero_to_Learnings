# authentication_window

import time
from selenium import webdriver

# Dynamically
username = "admin"
password = "admin"
url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.quit()
