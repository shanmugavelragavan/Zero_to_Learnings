# Mouse Hover Action 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.naukri.com")

try:
    wait = WebDriverWait(driver, 10)

    # Wait and locate the "Jobs"
    jobs = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[2]/nav/ul/li[1]/a/div')))

    # Wait and locate the "IT Jobs"
    it_jobs = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[4]/div[2]/nav/ul/li[1]/div/ul[1]/li[2]/a/div')))

    # Mouse hover and click
    actions = ActionChains(driver)
    actions.move_to_element(jobs).move_to_element(it_jobs).click().perform()

    print("Successfully clicked on IT Jobs!")
except Exception as e:
    print("Error:", e)
finally:
    driver.quit()
