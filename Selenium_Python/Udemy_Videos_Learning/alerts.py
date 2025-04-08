from selenium import webdriver
from selenium.webdriver.common.by import By
import time

name = "Shanmugavel"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print("Alert Message:", alert_text)
assert name in alert_text, "Name not found in alert message!"
alert.accept()
time.sleep(2)
driver.quit()