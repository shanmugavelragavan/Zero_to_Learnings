# Handle Alert | Types of Alert 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("http://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.maximize_window()
driver.implicitly_wait(3)

# Handling Simple Alert
driver.find_element(By.XPATH, '//*[@id="alertexamples"]').click()
time.sleep(2)  
driver.switch_to.alert.accept()

# Handling Confirmation Alert
driver.find_element(By.XPATH, '//*[@id="confirmexample"]').click()
time.sleep(2)
alert = driver.switch_to.alert
print("Alert Text:", alert.text)
alert.dismiss()

# Handling Prompt Alert
driver.find_element(By.XPATH, '//*[@id="promptexample"]').click()
time.sleep(2)
alert = driver.switch_to.alert
alert.send_keys("Shanmugavel")
time.sleep(2)
alert.accept()

# Time for page to Wait and Close the browser
time.sleep(3)
driver.quit()
