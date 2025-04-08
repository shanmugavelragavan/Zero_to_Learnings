# Handle Dropdown without using Select Class

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(10)

# Click to open the dropdown menu
driver.find_element(By.XPATH, '//*[@id="account_dd"]/div[1]/span').click()

# Find all dropdown options
options = driver.find_elements(By.XPATH, '//*[@id="account_dd"]/div[2]/ul/li')

# Loop run and  find "Show My Ticket"
for option in options:
    if option.text.strip() == "Show My Ticket":
        option.click()
        break

# Time for page to Wait and print mgs
time.sleep(3)
print("Successfully Clicked 'Show My Ticket'")

# Close the browser
driver.quit()

