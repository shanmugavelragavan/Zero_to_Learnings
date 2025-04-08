# Find Elements 

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Naukri website
driver.get("https://www.naukri.com/")
driver.maximize_window()

# Implicit Wait Before Interacting
driver.implicitly_wait(10)

# Find all a Tags
listA = driver.find_elements(By.TAG_NAME, "a")

# Print the total number of links
print("Total links found:", len(listA))

# Print first 10 links
for i, link in enumerate(listA[:10]):  
    print(f"Link {i+1}: {link.get_attribute('href')}")

# Close the browser
driver.quit()
