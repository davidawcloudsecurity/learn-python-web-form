from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Setup Chrome options for headless mode and other necessary arguments
chrome_options = Options()
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--headless")

# Setup ChromeDriver. Run chrome driver from dockerfile
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to Facebook
    driver.get("https://www.facebook.com")

    # Fill in username and password
    username = "david"
    password = "your_password"

    username_field = driver.find_element(By.ID, "email")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys(password)

    # Submit the login form
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()

    # Wait for a few seconds to let the page load
    time.sleep(5)

    # Print the current page title (for verification)
    print("Page Title:", driver.title)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser session
    driver.quit()
