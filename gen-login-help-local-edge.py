from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# This containers api docs, help centre then user name.
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
project_name = credentials.get('project_name')

# Set Edge options to run headless
edge_options = Options()
# edge_options.add_argument("--headless")  # Uncomment to run headless
# edge_options.add_argument("--window-size=1920x1080")

# Path to msedgedriver executable
edgedriver_path = r'.\edgedriver_win64\msedgedriver.exe'

# Initialize the EdgeDriver service
service = Service(executable_path=edgedriver_path)

# Initialize the Edge browser with the specified options
browser = webdriver.Edge(service=service, options=edge_options)

# Navigate to the specified login page
browser.get(website)

try:
    # Wait for the username input field to be present and visible
    username_field = WebDriverWait(browser, 60).until(
        EC.visibility_of_element_located((By.ID, "i0116"))
    )
    print("Enter username:", browser.title)

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
    print("Enter password:", browser.title)

    # Assuming there is a password field (update the selector to match the password field's attributes)
    password_field = WebDriverWait(browser, 60).until(
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

    # Wait for the div element to be visible
    display_sign_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.displaySign"))
    )

    # Get the text content of the div
    display_sign_text = display_sign_element.text
    print("Text in displaySign div:", display_sign_text)
      
    # Wait up to 10 seconds for the element to be clickable
    element = WebDriverWait(browser, 60).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@qa-id='menu-Projects']"))    
    )
    print("Genexis console:", browser.title)

    # Wait for at the profile to be clickable
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[qa-id='user-menu']"))
    )    

    # Click the button
    button.click()

    # Wait for the button to be clickable
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[qa-id='menu-item-help']"))
    )

    # Click the button
    button.click()
    print("Clicked on the 'Self-Help' button.")
    print("Self-Help Page:", browser.title)

    # Wait for the button to be clickable
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[qa-id='btn-tab-API Docs']"))
    )

    # Print the text to the terminal
    print("Clicked on the 'API Docs' button.")
    
    # Click the button
    button.click()

        # Wait for the button to be clickable
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, '/profile')]"))
    )

    # Print the text to the terminal
    print("Clicked on the 'Get /profile' button.")
    
    # Click the button
    button.click()

    # Wait for the button to be clickable
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Help Centre')]"))
    )
    
    # Click the button
    button.click()

    # Wait for the SVG/mail icon element to be clickable (assuming you are targeting the entire SVG)
    svg_element = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg.chakra-icon.css-n17ngm"))
    )

    # Click the SVG element
    svg_element.click()
    print("Clicked on the SVG element.")    


    # Wait for the button to be clickable based on qa-id attribute
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@qa-id='btn-tab-User Manual']"))
    )

    # Click the button
    button.click()    

    # Wait for the button to be clickable
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Getting Started')]"))
    )
    
    # Click the button
    button.click()

    # Wait for the button to be clickable
    button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='chakra-button css-1cr14s9']"))
    )

    # Print the text to the terminal
    print(f"Clicked on the: 1.1.1 Log in to GeneXis")
    
    # Click the button
    button.click()    

#    prioritize_button = WebDriverWait(browser, 10).until(
#        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[qa-id='project-d3382591-c70c-47af-887e-a47ce87f2bf3-prioritize-btn']"))
#    )
    
#    prioritize_button.click()
#    print("Clicked on the 'Pin' button.")    

except (NoSuchElementException, TimeoutException) as e:
    print(f"An element was not found or the operation timed out: {e}")

input('Press anything to quit')

# Close the browser session
browser.quit()
