# Automate Webpage Scrolling

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()

# Scroll down by 100 pixels
driver.execute_script("window.scrollBy(0, 100)")
time.sleep(3)

# Wait for the element and scroll into view
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="standard-collection-wdgt"]/div/h2'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
except Exception as e:
    print("Element not found:", e)
    time.sleep(3)

# Scroll to the bottom of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(3)

# Scroll up by 100 pixels
driver.execute_script("window.scrollBy(0, -100)")
time.sleep(3)

# Close the browser
driver.quit()
