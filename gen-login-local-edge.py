from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Function to read credentials from file
def read_credentials(filename):
    credentials = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if '=' in line:
                    key, value = line.split('=', 1)
                    credentials[key] = value
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return credentials

# Read credentials from the file
credentials = read_credentials('cred.txt')
username = credentials.get('username')
password = credentials.get('password')
website = credentials.get('website')

# Set Edge options to run headless
edge_options = Options()
# edge_options.add_argument("--headless")  # Uncomment to run headless
# edge_options.add_argument("--window-size=1920x1080")

# Path to msedgedriver executable
edgedriver_path = r'C:\Users\admin\Downloads\learn-python-web-form\edgedriver_win64\msedgedriver.exe'

# Initialize the EdgeDriver service
service = Service(executable_path=edgedriver_path)

# Initialize the Edge browser with the specified options
browser = webdriver.Edge(service=service, options=edge_options)

# Navigate to the specified login page
browser.get(website)

try:
    # Wait for the username input field to be present and visible
    username_field = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "i0116"))
    )

    # Ensure the field is interactable
    if username_field.is_displayed() and username_field.is_enabled():
        username_field.send_keys(username)
        print("Username entered successfully.")
    else:
        print("Username field is not interactable.")

    # Find the submit button and click it (update the selector to match the submit button's attributes)
    submit_button = browser.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    print("Submit button clicked.")

    # Wait for a few seconds to let the page load
    time.sleep(5)
    print("Page Title:", browser.title)

    # Assuming there is a password field (update the selector to match the password field's attributes)
    password_field = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "i0118"))  # Update the ID to match the actual password field ID
    )

    if password_field.is_displayed() and password_field.is_enabled():
        password_field.send_keys(password)
        print("Password entered successfully.")
    else:
        print("Password field is not interactable.")

    submit_button = browser.find_element(By.XPATH, "//input[@id='idSIButton9']")
    submit_button.click()
    print("Sign in button clicked.")
        
    # Wait for the h2 element to be present and visible
    welcome_message_element = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "chakra-heading css-1m1d22u"))
    )

    # Print the text of the h2 element
    print("Test")
    print(welcome_message_element.text)
except (NoSuchElementException, TimeoutException) as e:
    print(f"An element was not found or the operation timed out: {e}")

input('Press anything to quit')

# Close the browser session
browser.quit()
