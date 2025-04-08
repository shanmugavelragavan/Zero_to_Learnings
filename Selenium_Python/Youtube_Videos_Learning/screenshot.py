# take Screenshot of a webpage

from selenium import webdriver
import time
from datetime import datetime

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")

# Wait for the page
time.sleep(3)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_filename = f"screenshot_{timestamp}.png"

# Take a screenshot and save
driver.save_screenshot(screenshot_filename)

# Print confirmation
print(f"Screenshot saved as {screenshot_filename}")

# Close the browser
driver.quit()
