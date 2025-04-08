# Navigate Forward and Backward | Refresh the Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Open first website
driver.get("https://www.redbus.in/")

# Navigate to Google
driver.get("https://www.google.co.in/")

# Go back to RedBus
driver.back()
WebDriverWait(driver, 10).until(EC.title_contains("redBus"))  # Wait until RedBus title appears
print("Current Page Title:", driver.title)

# Go forward to Google
driver.forward()
WebDriverWait(driver, 10).until(EC.title_contains("Google"))  # Wait until Google title appears
print("Current Page Title:", driver.title)

# Refresh the page
driver.refresh()

# Close the browser
driver.quit()
