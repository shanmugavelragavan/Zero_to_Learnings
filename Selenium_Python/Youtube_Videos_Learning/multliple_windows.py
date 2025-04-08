# Handle Multliple Windows

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.naukri.com")
driver.maximize_window()

# Wait for the link to be clickable
try:
    wait = WebDriverWait(driver, 10)
    link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="trending-naukri-wdgt"]/div/div[1]/a[2]/span')))
    link.click()
except Exception as e:
    print("Element not found:", e)

# Window handle
parent = driver.current_window_handle
print("Parent Window Handle:", parent)

# Get all window handles
all_handles = driver.window_handles

# All open windows
for handle in all_handles:
    driver.switch_to.window(handle)
    print("Window Title:", driver.title)
    if handle != parent:
        driver.close()

# Switch back to the window
driver.switch_to.window(parent)

# Close the browser
driver.quit()
