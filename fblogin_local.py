from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Set Chrome options to run headless
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1920x1080")

# Path to chromedriver executable
chromedriver_path = r'C:\Users\.\Downloads\learn-python-web-form\chromedriver_win32\chromedriver.exe'

# Initialize the ChromeDriver service
service = Service(executable_path=chromedriver_path)

# Initialize the Chrome browser with the specified options
browser = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Facebook login page
browser.get("https://facebook.com")

try:
    # Find the username and password input fields and fill them in
    username_field = browser.find_element(By.XPATH, "//*[@id='email']")
    username_field.send_keys("David")

    password_field = browser.find_element(By.XPATH, "//*[@id='pass']")
    password_field.send_keys("Password")

    # Find the login button and click it using its name attribute
    login_button = browser.find_element(By.NAME, 'login')
    login_button.click()

    # Wait for a few seconds to let the page load
    time.sleep(5)

    # Print the current page title (for demonstration)
    print("Page Title:", browser.title)
except NoSuchElementException as e:
    print(f"An element was not found: {e}")

input('Press anything to quit')

# Close the browser session
browser.quit()
