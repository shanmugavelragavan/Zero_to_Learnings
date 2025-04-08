# Handle Dropdown Using Select Class

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Rediff Registration Page
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.implicitly_wait(10)

# Locate Month Dropdown
month = driver.find_element(By.XPATH, "//select[contains(@name,'DOB_Month')]")

# Create Select Object for Dropdown
month_option = Select(month)

# Select Month by Index
month_option.select_by_index(2)
time.sleep(3)

# Select Month by Value
month_option.select_by_value("07")
time.sleep(3)

# Select Month by Visible Text
month_option.select_by_visible_text("OCT")
time.sleep(3)

# Get All Options in the Dropdown
options = month_option.options

# Print the Total Number of Options
print("Total options : ", len(options))

# Print Each Option's Text
for option in options:
    print(option.text)

# Close the browser
driver.quit()
