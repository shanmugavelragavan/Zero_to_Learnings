# Selenium in Python provides various modules and imports for web automation.
# Below is a detailed explanation of the most commonly used imports along with their functionalities.


# 1. Basic Selenium Imports

from selenium import webdriver # Import Webdriver to control the browser
from selenium.webdriver.common.by import By # Locator strategies
from selenium.webdriver.common.keys import Keys  # Keyboard actions
from selenium.webdriver.common.action_chains import ActionChains  # Mouse actions
from selenium.webdriver.common.alert import Alert  # Handling alerts
from selenium.webdriver.common.window import WindowTypes  # Window management
from selenium.webdriver.chrome.service import Service  # WebDriver service
from selenium.webdriver.chrome.options import Options  # Browser options
import time  # Used for sleep delays


# 2. WebDriver and Browser Options
# Selenium provides different browser drivers like Chrome, Edge, and Firefox.

# i} Chrome WebDriver Example
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
driver.quit()

# Other Browsers
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# ii} Firefox
driver = webdriver.Firefox(service=FirefoxService("geckodriver.exe"))

# iii} Edge
driver = webdriver.Edge(service=EdgeService("msedgedriver.exe"))


# 3. Locators (Finding Elements)

from selenium.webdriver.common.by import By

driver.find_element(By.ID, "element_id")  # Find by ID
driver.find_element(By.NAME, "element_name")  # Find by Name
driver.find_element(By.CLASS_NAME, "class_name")  # Find by Class Name
driver.find_element(By.TAG_NAME, "tag_name")  # Find by Tag Name
driver.find_element(By.LINK_TEXT, "Exact Link Text")  # Find by Link Text
driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Link")  # Find by Partial Link Text
driver.find_element(By.XPATH, "//tagname[@attribute='value']")  # Find by XPATH
driver.find_element(By.CSS_SELECTOR, "css_selector")  # Find by CSS Selector


# 4. Handling Keyboard Inputs
# For simulating keyboard actions, we use `Keys`:

from selenium.webdriver.common.keys import Keys

element = driver.find_element(By.NAME, "q")  # Example: Google Search Box
element.send_keys("Selenium Python" + Keys.RETURN)  # Type and press Enter


# 5. Handling Mouse Actions
# To perform drag-and-drop, hover, right-click, etc., we use `ActionChains`:

from selenium.webdriver.common.action_chains import ActionChains

element = driver.find_element(By.ID, "some_id")
actions = ActionChains(driver)
actions.move_to_element(element).perform()  # Hover over an element
actions.click(element).perform()  # Click on the element
actions.double_click(element).perform()  # Double click
actions.context_click(element).perform()  # Right click


# 6. Handling JavaScript Alerts
# For handling browser alerts:

from selenium.webdriver.common.alert import Alert

alert = Alert(driver)
alert.accept()  # Clicks OK on alert
alert.dismiss()  # Clicks Cancel on alert
alert.send_keys("Some text")  # Sends text input in prompt alert


# 7. Handling Frames and iFrames
# If an element is inside an iframe, you need to switch to it:

driver.switch_to.frame("frame_name")  # Switch by Name
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))  # Switch by Element
driver.switch_to.default_content()  # Switch back to the main page


# 8. Handling Windows and Tabs
# If multiple browser tabs/windows are opened, switch between them:

windows = driver.window_handles
driver.switch_to.window(windows[1])  # Switch to second tab
driver.close()  # Close current tab
driver.switch_to.window(windows[0])  # Switch back to first tab


# 9. Handling Waits
# Instead of using `time.sleep()`, Selenium provides better wait mechanisms.

# Implicit Wait (Applies globally)

driver.implicitly_wait(10)  # Waits for 10 seconds before throwing an error

# Explicit Wait (Waits for a specific condition)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))  # Wait until element appears



# 10. Running Selenium in Headless Mode
# If you want Selenium to run without opening a browser window:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(options=options)


# 11. Taking Screenshots

driver.save_screenshot("screenshot.png")  # Saves screenshot of the whole page
