# Handle Frames/iframes

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.rediff.com/")

try:
    # iframe and switch
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(("name", "moneyiframe")))

    # Locate and print BSE index value
    bsc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bseindex")))
    print("BSE Index:", bsc.text)

    # Switch back page
    driver.switch_to.default_content()

    # Click on "Business Email" link
    business_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Business Email")))
    business_email.click()

    print("Business Email link clicked successfully!")

except Exception as e:
    print("Error:", e)

finally:
    time.sleep(3)
    driver.quit()
