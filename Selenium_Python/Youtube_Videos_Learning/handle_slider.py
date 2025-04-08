# Handle Slider

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.snapdeal.com/products/electronics-home-audio-systems?sort=plrty&q=Price%3A7054%2C7054%7C")

try:
    wait = WebDriverWait(driver, 10)

    # left slider and move it
    left = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content_wrapper"]/div[9]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[1]')))
    actions = ActionChains(driver)
    actions.click_and_hold(left).move_by_offset(50, 0).release().perform()

    # right slider and move it
    right = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content_wrapper"]/div[9]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[2]')))
    actions.click_and_hold(right).move_by_offset(-30, 0).release().perform()

    print("Sliders moved successfully!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
