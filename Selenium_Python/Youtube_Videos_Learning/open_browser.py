# Running First Selenium Python Script 

from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open YouTube 
driver.get("https://www.youtube.com/")

# Maximize the window
driver.maximize_window()

# Time for page to Wait
time.sleep(3)

# Print the page title
print("Page Title : ", driver.title)

# Minimize the window
driver.minimize_window()

# Close the browser
driver.quit()
