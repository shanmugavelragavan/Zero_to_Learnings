from selenium import webdriver
from selenium.webdriver.common.by import By


def select_checkbox(option_value):
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")

        checkBoxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
        print(len(checkBoxes))
        for checkBox in checkBoxes:
            if checkBox.get_attribute("value") == option_value:
                checkBox.click()
                assert checkBox.is_selected()
                break

        radio_btns = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
        radio_btns[2].click()  # type: ignore
        assert radio_btns[2].is_selected()  # type: ignore

        assert driver.find_element(By.ID, "displayed-text").is_displayed()

        driver.find_element(By.ID, "hide-textbox").click()

        assert not driver.find_element(By.ID, "displayed-text").is_displayed()
    finally:
        driver.quit()


# Call the function with the desired option value
select_checkbox("option2")
