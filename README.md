# learn-python-web-form
how to fill web form with python

```ruby
Old API                          New API
find_element_by_id(‘id’)         find_element(By.ID, ‘id’)
find_element_by_name(‘name’)     find_element(By.NAME, ‘name’)
find_element_by_xpath(‘xpath’)	 find_element(By.XPATH, ‘xpath’)
```
https://www.lambdatest.com/blog/selenium-click-button-with-examples/

https://uilicious.com/blog/how-to-click-a-button-using-selenium/
## Run Selenium with docker
```ruby
pip install selenium

docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest
```
## Change to edge
```ruby
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

# Navigate to Facebook login page
browser.get("https://facebook.com")

time.sleep(60)

input('Press anything to quit')

# Close the browser session
browser.quit()

```
# Start here
```ruby
How to
https://softwaresennin.medium.com/never-fill-out-another-boring-online-form-use-python-to-make-it-automatic-e84afa6b066a

Using xpath
https://www.youtube.com/watch?v=B5X2nyA8RlU

Using name/id
https://www.youtube.com/watch?v=doPo9q6on6c

dockerise python with selenium
https://www.youtube.com/watch?v=xrYDlx8evR0
https://blog.devgenius.io/docker-python-selenium-the-quickest-way-to-start-web-scraping-6c47248c69c3

how to use it on nodejs
https://stackoverflow.com/questions/54352702/selenium-find-element-via-data-qa-attribute
https://www.geeksforgeeks.org/get_attribute-element-method-selenium-python/
```
https://github.com/swhasans/Auto-Fill

https://softwaresennin.medium.com/never-fill-out-another-boring-online-form-use-python-to-make-it-automatic-e84afa6b066a

https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/

Run docker

https://blog.devgenius.io/docker-python-selenium-the-quickest-way-to-start-web-scraping-6c47248c69c3

https://nander.cc/using-selenium-within-a-docker-container

https://stackoverflow.com/questions/45323271/how-to-run-selenium-with-chrome-in-docker

https://ahsonshaikh616.medium.com/streamlined-selenium-grid-setup-running-selenium-code-with-selenium-standalone-chrome-docker-image-c3355bc850e4

https://gpt.com/share/77c7a5e2-7a0a-45a3-a4ea-e026d7a22fc6

Create file
```bash
username=<username>
password=<password>
website=<url>
project_name=<name>
```
