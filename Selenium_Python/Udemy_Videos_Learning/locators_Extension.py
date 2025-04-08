from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/client/")
    return driver

def fill_reset_form(driver):
    driver.find_element(By.LINK_TEXT, "Forgot password?").click()
    driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Fresh$321")
    driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Fresh$321")
    sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
    # (OR)
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()

def main():
    driver = initialize_driver()
    fill_reset_form(driver)
    sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()