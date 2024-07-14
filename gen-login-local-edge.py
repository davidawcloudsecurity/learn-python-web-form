from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

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
browser.get("https://example.com")

try:
    # Wait for the username input field to be present and visible
    username_field = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "i0116"))
    )

    # Ensure the field is interactable
    if username_field.is_displayed() and username_field.is_enabled():
        username_field.send_keys("username@example.com")
        print("Username entered successfully.")
    else:
        print("Username field is not interactable.")

    # Find the submit button and click it (update the selector to match the submit button's attributes)
    submit_button = browser.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()
    print("Submit button clicked.")

    # Wait for a few seconds to let the page load
    time.sleep(5)

    # Print the current page title (for demonstration)
    print("Page Title:", browser.title)
except (NoSuchElementException, TimeoutException) as e:
    print(f"An element was not found or the operation timed out: {e}")

input('Press anything to quit')

# Close the browser session
browser.quit()
