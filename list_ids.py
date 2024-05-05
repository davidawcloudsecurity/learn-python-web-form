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
browser.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_login_form_modal")

ids = browser.find_elements(By.XPATH, '//*[@id]')
# to get names use '//*[@name]'

for ii in ids:
    print('Tag: ' + ii.tag_name)
    print('ID: ' + ii.get_attribute('id'))  # Element id as a string
    # Check if the 'name' attribute exists before concatenating
    name_attribute = ii.get_attribute('name')
    if name_attribute:
        print('Name: ' + name_attribute)  # Element name as a string
    else:
        print('Name: None')  # No 'name' attribute found

# Wait for a few seconds to let the page load
time.sleep(5)

# Print the current page title (for demonstration)
print("Page Title:", browser.title)
input('Press anything to quit')
# Close the browser session
browser.quit()
