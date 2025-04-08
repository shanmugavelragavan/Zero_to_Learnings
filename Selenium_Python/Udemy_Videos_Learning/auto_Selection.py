from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
    return driver

def select_country(driver, country_name):
    autosuggest = driver.find_element(By.ID, "autosuggest")
    autosuggest.send_keys("ind")
    sleep(2)  # Wait for suggestions to load

    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print(len(countries))

    for country in countries:
        if country.text == country_name:
            country.click()
            break
    else:
        print("No matching country found!")

    assert autosuggest.get_attribute("value") == country_name

def main():
    driver = initialize_driver()
    select_country(driver, "India")
    sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()
