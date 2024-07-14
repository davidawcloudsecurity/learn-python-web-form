import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class TestWebPage(unittest.TestCase):
    def setUp(self):
        # Set up your WebDriver (assuming you're using Edge as per previous examples)
        edge_options = Options()
        # edge_options.add_argument("--headless")  # Uncomment to run headless
        # edge_options.add_argument("--window-size=1920x1080")

        # Path to msedgedriver executable
        edgedriver_path = r'.\edgedriver_win64\msedgedriver.exe'

        # Initialize the EdgeDriver service
        service = Service(executable_path=edgedriver_path)

        # Initialize the Edge browser with the specified options
        self.browser = webdriver.Edge(service=service, options=edge_options)

    def tearDown(self):
        # Clean up resources after each test method
        self.browser.quit()

    def test_access_project(self):
        try:
            # Read credentials and project name from a file
            credentials = self.read_credentials('cred.txt')
            username = credentials.get('username')
            password = credentials.get('password')
            website = credentials.get('website')
            project_name = credentials.get('project_name')

            # Navigate to the login page
            self.browser.get(website)

            # Login process
            self.login(username, password)

            # Access project
            self.access_project(project_name)

            # Check if project can be accessed
            self.check_project_access(project_name)

        except (NoSuchElementException, TimeoutException) as e:
            self.fail(f"An element was not found or the operation timed out: {e}")

    def read_credentials(self, filename):
        credentials = {}
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if '=' in line:
                        key, value = line.split('=', 1)
                        credentials[key] = value
        except FileNotFoundError:
            self.fail(f"The file {filename} does not exist.")
        except Exception as e:
            self.fail(f"An error occurred while reading the file: {e}")
        return credentials

    def login(self, username, password):
        try:
            # Wait for the username input field to be present and visible
            username_field = WebDriverWait(self.browser, 60).until(
                EC.visibility_of_element_located((By.ID, "i0116"))
            )
            print("Enter username:", self.browser.title)

            # Enter username
            username_field.send_keys(username)
            print("Username entered successfully.")

            # Find and click submit button
            submit_button = self.browser.find_element(By.XPATH, "//input[@type='submit']")
            submit_button.click()
            print("Submit button clicked.")

            # Wait for the password input field to be present and visible
            password_field = WebDriverWait(self.browser, 60).until(
                EC.visibility_of_element_located((By.ID, "i0118"))
            )
            print("Enter password:", self.browser.title)

            # Enter password
            password_field.send_keys(password)
            print("Password entered successfully.")

            # Find and click sign in button
            submit_button = self.browser.find_element(By.XPATH, "//input[@id='idSIButton9']")
            submit_button.click()
            print("Sign in button clicked.")

            # Wait for the div element to be visible
            display_sign_element = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.displaySign"))
            )

            # Get the text content of the div
            display_sign_text = display_sign_element.text
            print("Text in displaySign div:", display_sign_text)


        except (NoSuchElementException, TimeoutException) as e:
            self.fail(f"Login failed: {e}")

    def access_project(self, project_name):
        try:
            # Find and click on 'Projects' link
            link = WebDriverWait(self.browser, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@qa-id='menu-Projects']"))
            )
            link.click()
            print("Clicked on 'Projects' link.")

            # Find and type project name in search field
            search_field = WebDriverWait(self.browser, 60).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[qa-id='search-project']"))
            )
            search_field.clear()
            search_field.send_keys(project_name)
            print(f"Typed '{project_name}' into the search field.")

            # Find and click on project link dynamically
            link = WebDriverWait(self.browser, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"a[qa-id*='{project_name}']"))
            )
            link.click()
            print(f"Clicked on the '{project_name}' project link.")

            # Wait for the 'Go to Internet Facing Project' button to be clickable
            button = WebDriverWait(self.browser, 60).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.chakra-button.css-1rwzulq[qa-id='btn-go-to-project']"))
            )
            button.click()
            print("Clicked on the 'Go to Internet Facing Project' button.")

            # Wait for the new window or tab to open
            current_window_handle = self.browser.current_window_handle
            WebDriverWait(self.browser, 60).until(EC.new_window_is_opened)
            new_window_handle = [handle for handle in self.browser.window_handles if handle != current_window_handle][0]
            self.browser.switch_to.window(new_window_handle)

            # Wait for the new window/tab to load
            time.sleep(10)
            print(f"URL of the new window/tab: {self.browser.current_url}")

        except (NoSuchElementException, TimeoutException) as e:
            self.fail(f"Failed to access project: {e}")

    def check_project_access(self, project_name):
        # Assert if the project URL contains the project_name
        self.assertIn(project_name, self.browser.current_url, "Project cannot be accessed.")

if __name__ == "__main__":
    unittest.main()
