# Handle Radio buttons

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Rediff Registration Page
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()

# Implicit Wait Before Interacting
driver.implicitly_wait(10)

# Radio Buttons
male_option = driver.find_element(By.XPATH, "//input[@value='m']")
female_option = driver.find_element(By.XPATH, "//input[@value='f']")

# Click on Female Option
female_option.click()

# Check Selection and Display Status
print("Is Female selected:", female_option.is_selected())
print("Is Female enabled:", female_option.is_enabled())
print("Is Female displayed:", female_option.is_displayed())
print("Is Male selected:", male_option.is_selected())

# Time for page to Wait
time.sleep(3)

# Close the browser
driver.quit()
