# Locators | ID , Partial link text , 
# link text , Class Name , NAME , 
# TAG_NAME , XPATH , CSS_SELECTOR

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

# 1. Finding element by Partial Link Text

driver.find_element(By.PARTIAL_LINK_TEXT, "Contact").click()

# 2. Finding element by Name

driver.find_element(By.NAME, "FullName").send_keys("Shanmugavel")

# 3. Finding element by ID

driver.find_element(By.ID, "Form_getForm_Contact").send_keys("1234567890")

# 4. Finding element by CSS_SELECTOR

driver.find_element(By.CSS_SELECTOR, '#Form_getForm_Email').send_keys("Shanmugavel@gmail.com")

# 5. Finding element by CLASS_NAME

driver.find_element(By.CLASS_NAME, "text").send_keys("Summa")

# 6. Finding element by XPATH

driver.find_element(By.XPATH, '//*[@id="Form_getForm_Comment"]').send_keys("Tailored Solutions: Our experienced sales team understands your organization's unique needs, offering customized options to match your requirements.")

# Close the browser

driver.quit()