import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://localhost:5000"

def get_driver():
    """Setup Chrome driver with headless options"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

class SeleniumTests(unittest.TestCase):

    def setUp(self):
        """Initialize browser before each test"""
        self.driver = get_driver()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Close browser after each test"""
        self.driver.quit()

    def test_01_home_page_title(self):
        """Test 1: Home page loads and has correct title"""
        self.driver.get(BASE_URL)
        time.sleep(1)
        title = self.driver.title
        self.assertIsNotNone(title)
        print(f"✅ Test 1 Passed: Page title is '{title}'")

    def test_02_page_has_form(self):
        """Test 2: Home page contains input form"""
        self.driver.get(BASE_URL)
        time.sleep(1)
        # Check name input exists
        name_input = self.driver.find_element(By.NAME, "name")
        message_input = self.driver.find_element(By.NAME, "message")
        self.assertIsNotNone(name_input)
        self.assertIsNotNone(message_input)
        print("✅ Test 2 Passed: Form inputs found on page")

    def test_03_submit_message(self):
        """Test 3: Submit a message through the form"""
        self.driver.get(BASE_URL)
        time.sleep(1)
        # Fill in the form
        name_input = self.driver.find_element(By.NAME, "name")
        message_input = self.driver.find_element(By.NAME, "message")
        name_input.clear()
        name_input.send_keys("Selenium Tester")
        message_input.clear()
        message_input.send_keys("This is a Selenium test message")
        # Submit the form
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()
        time.sleep(2)
        # Check we are back on home page
        self.assertIn("localhost:5000", self.driver.current_url)
        print("✅ Test 3 Passed: Message submitted successfully")

    def test_04_message_appears_after_submit(self):
        """Test 4: Submitted message appears on page"""
        self.driver.get(BASE_URL)
        time.sleep(1)
        # Submit a unique message
        name_input = self.driver.find_element(By.NAME, "name")
        message_input = self.driver.find_element(By.NAME, "message")
        name_input.send_keys("LaibaTester")
        message_input.send_keys("UniqueTestMsg123")
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()
        time.sleep(2)
        # Check message appears on page
        page_source = self.driver.page_source
        self.assertIn("LaibaTester", page_source)
        print("✅ Test 4 Passed: Message appears on page after submission")

    def test_05_page_loads_fast(self):
        """Test 5: Page loads within acceptable time"""
        start = time.time()
        self.driver.get(BASE_URL)
        end = time.time()
        load_time = end - start
        self.assertLess(load_time, 10)
        print(f"✅ Test 5 Passed: Page loaded in {load_time:.2f} seconds")

    def test_06_multiple_messages(self):
        """Test 6: Multiple messages can be submitted"""
        self.driver.get(BASE_URL)
        time.sleep(1)
        # Submit first message
        self.driver.find_element(By.NAME, "name").send_keys("User1")
        self.driver.find_element(By.NAME, "message").send_keys("First Message")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        # Submit second message
        self.driver.find_element(By.NAME, "name").send_keys("User2")
        self.driver.find_element(By.NAME, "message").send_keys("Second Message")
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        page_source = self.driver.page_source
        self.assertIn("User1", page_source)
        self.assertIn("User2", page_source)
        print("✅ Test 6 Passed: Multiple messages displayed correctly")

if __name__ == '__main__':
    unittest.main(verbosity=2)
