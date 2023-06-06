import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
firefox_binary_path = os.environ.get("FIREFOX_BINARY_PATH")
geckodriver_path = os.environ.get("GECKODRIVER_PATH")
app_url = "https://staging.mindplex.ai/"

driver = webdriver.Firefox(firefox_binary=firefox_binary_path, executable_path=geckodriver_path)
driver.get(app_url)

anchor_elements = driver.find_elements(By.CSS_SELECTOR, "a.header-links")
anchor_hyperlinks = []
for element in anchor_elements:
    anchor_hyperlinks.append(element.get_attribute("href"))

for hyperlink in anchor_hyperlinks:
    driver.get(hyperlink)
    time.sleep(2)
    if driver.title:
        print("Successfully opened: " + driver.title + " - " + hyperlink)
    else:
        print("Failed to open: " + hyperlink)

driver.quit()