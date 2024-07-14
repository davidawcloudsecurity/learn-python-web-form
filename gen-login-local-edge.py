from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
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
browser.get("https://stag.genexis.gov.sg")

time.sleep(60)

try:
    # Find the username input field and fill it in
    username_field = browser.find_element(By.ID, "i0116")
    username_field.send_keys("David")

    # Find the submit button and click it (update the selector to match the submit button's attributes)
    submit_button = browser.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    # Wait for a few seconds to let the page load
    time.sleep(5)

    # Print the current page title (for demonstration)
    print("Page Title:", browser.title)
except NoSuchElementException as e:
    print(f"An element was not found: {e}")

input('Press anything to quit')

# Close the browser session
browser.quit()
