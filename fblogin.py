from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Set Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

# Path to chromedriver executable

# Initialize the Chrome browser with the specified options
browser = webdriver.Remote("http://localhost:4444", options=webdriver.ChromeOptions())

# Navigate to Facebook login page
browser.get("https://www.facebook.com")

# Find the username and password input fields and fill them in
username_field = browser.find_element(By.XPATH, "//*[@id='email']")
username_field.send_keys("David")

password_field = browser.find_element(By.XPATH, "//*[@id='pass']")
password_field.send_keys("Password")

# Find the login button and click it using XPath
login_button = browser.find_element(By.ID, 'loginbutton')
# login_button = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
login_button.click()

# Wait for a few seconds to let the page load
time.sleep(5)

# Print the current page title (for demonstration)
print("Page Title:", browser.title)
input('Press anything to quit')
# Close the browser session
browser.quit()
