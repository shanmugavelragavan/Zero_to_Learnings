from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
sleep(3)
results = driver.find_elements(By.XPATH, '//div[@class="products"]/div')
count = len(results)
assert count > 0
for result in results:
  result.find_element(By.XPATH, "div/button").click()
driver.find_element(By. CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, '//*[@id="root"]/div/header/div/div[3]/div[2]/div[2]/button').click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)