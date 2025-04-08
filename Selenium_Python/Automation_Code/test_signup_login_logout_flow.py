import unittest
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pyttsx3
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class StreamFlixAutomationTest(unittest.TestCase):
    
    def setUp(self):
        # Set up test environment before each test case
        logger.info("Setting up test environment")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        # Initialize voice engine
        self.voice_engine = pyttsx3.init()
        self.voice_engine.setProperty('rate', 150)
        
        # Base URL
        self.base_url = "https://stream-fix.netlify.app/"
        
        # Expert names to use
        self.expert_names = ["Shanmugavel", "Ragavan", "Thiruppathi", "Rajesh", "Saravanan"]
        self.expert_password = ["Shanmu@78100", "Ragavan@M8N", "Thi1$404", "Rajesh$321", "Saravanan@123"]
        
        # Select random expert name
        self.random_name = random.choice(self.expert_names)
        
        # Generate random email
        self.random_email = f"user_{self._generate_random_string(8)}@example.com"
        
        # Fixed password
        self.random_password = random.choice(self.expert_password)
        
        logger.info(f"Using credentials - Name: {self.random_name}, Email: {self.random_email}, Password: {self.random_password}")
        
        # Store for later use in login
        self.test_data = {
            "name": self.random_name,
            "email": self.random_email,
            "password": self.random_password
        }
    
    def _generate_random_string(self, length):
        # Generate a random alphanumeric string
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
        
    def _voice_announce(self, message):
        # Announce a step using voice
        logger.info(f"Voice: {message}")
        self.voice_engine.say(message)
        self.voice_engine.runAndWait()
    
    def _wait_and_click(self, by, value, timeout=10, voice_message=None):
        # Wait for an element to be clickable and click it
        try:
            if voice_message:
                self._voice_announce(voice_message)
                    
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            return True
        except TimeoutException:
            logger.error(f"Element not clickable: {by}={value}")
            return False
    
    def _wait_and_fill(self, by, value, text, timeout=10, voice_message=None):
        # Wait for an element to be visible and fill it with text
        try:
            if voice_message:
                self._voice_announce(voice_message)
                
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            logger.error(f"Element not visible: {by}={value}")
            return False
    
    def test_signup_login_logout_flow(self):
        # Test the full flow: signup, logout, login
        
        # Step 1: Open the home page
        self._voice_announce("Starting StreamFlix automation test")
        self.driver.get(self.base_url)
        logger.info("Opened homepage")
        
        # Wait for page to load completely
        time.sleep(2)
        
        # Step 2: Navigate to login page
        self._wait_and_click(By.XPATH, "/html/body/header/div/div[2]/div[1]/a/p", voice_message="Clicking on login link")
        
        # Step 3: Navigate to sign up page
        self._wait_and_click(By.XPATH, '//*[@id="form"]/a', voice_message="Clicking on sign up link")
        
        # Step 4: Fill sign up form
        self._voice_announce("Filling sign up form")
        self._wait_and_fill(By.ID, "name", self.test_data["name"], voice_message="Entering name")
        self._wait_and_fill(By.ID, "email", self.test_data["email"], voice_message="Entering email")
        self._wait_and_fill(By.ID, "password", self.test_data["password"], voice_message="Entering password")
        
        # Click sign up button
        self._wait_and_click(By.ID, "btn", voice_message="Clicking sign up button")
        
        # Step 5: Handle sign up confirmation popup
        try:
            # Wait for popup to appear
            WebDriverWait(self.driver, 10).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            self._voice_announce("Sign up successful. Accepting alert.")
            alert.accept()
        except TimeoutException:
            logger.error("No alert appeared after signup")
            self._voice_announce("No confirmation popup appeared")
            
        # Wait for redirect to home page
        time.sleep(3)
        
        # Step 6: Perform logout
        self._voice_announce("Now logging out")
        self._wait_and_click(By.XPATH, "/html/body/header/div/div[2]/div[1]", voice_message="Clicking profile button")
        self._wait_and_click(By.XPATH, "/html/body/header/div/div[2]/div[2]/div[4]", voice_message="Clicking logout button")
        
        # Handle logout confirmation
        try:
            WebDriverWait(self.driver, 10).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            self._voice_announce("Logout successful. Accepting alert.")
            alert.accept()
        except TimeoutException:
            logger.error("No alert appeared after logout")
            self._voice_announce("No logout confirmation popup appeared")
        
        # Wait for redirect
        time.sleep(2)
        
        # Step 7: Navigate back to login page
        self._wait_and_click(By.XPATH, "/html/body/header/div/div[2]/div[1]/a/p", voice_message="Going back to login page")
        
        # Step 8: Perform login with previously created credentials
        self._voice_announce("Now logging in with created account")
        self._wait_and_fill(By.ID, "email", self.test_data["email"], voice_message="Entering email")
        self._wait_and_fill(By.ID, "password", self.test_data["password"], voice_message="Entering password")
        self._wait_and_click(By.ID, "btn", voice_message="Clicking login button")
        
        # Handle login confirmation
        try:
            WebDriverWait(self.driver, 10).until(
                EC.alert_is_present()
            )
            alert = self.driver.switch_to.alert
            self._voice_announce("Login successful. Accepting alert.")
            alert.accept()
        except TimeoutException:
            logger.error("No alert appeared after login")
            self._voice_announce("No login confirmation popup appeared")
        
        # Verify we're on the home page by checking for content
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/header/div/div[1]/a/h2"))
            )
            self._voice_announce("Successfully logged in and reached home page")
            logger.info("Test completed successfully")
        except TimeoutException:
            logger.error("Failed to reach home page after login")
            self._voice_announce("Test failed. Could not verify successful login.")
            self.fail("Could not verify successful login")
    
    def tearDown(self):
        """Clean up after each test case"""
        self._voice_announce("Test complete. Closing browser.")
        logger.info("Tearing down test environment")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()