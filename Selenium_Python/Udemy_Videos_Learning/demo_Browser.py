from selenium import webdriver
from time import sleep

def initialize_driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com")
    return driver

def main():
    driver = initialize_driver()
    print("Title:", driver.title)
    print("Current URL:", driver.current_url)
    sleep(5)
    driver.quit()

if __name__ == "__main__":
    main()