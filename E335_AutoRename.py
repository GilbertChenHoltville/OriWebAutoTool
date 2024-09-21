from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Set up the Chrome options to connect to existing session
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Connect to the existing Chrome session
driver = webdriver.Chrome(options=options)

#read website.txt
with open("./website.txt", "r") as file:
    str_address = file.read()
    print("opening",str_address)
    # exit()

# Navigate to your SharePoint page (if not already there)
driver.get(str_address)


