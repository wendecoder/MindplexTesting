from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

firefox_binary_path = os.environ.get("FIREFOX_BINARY_PATH")
print(firefox_binary_path)

geckodriver_path = os.environ.get("GECKODRIVER_PATH")
print(geckodriver_path)
driver = webdriver.Firefox(firefox_binary=firefox_binary_path, executable_path=geckodriver_path)


driver.get("https://staging.mindplex.ai/")

button = driver.find_element(By.ID, "signup")
time.sleep(15)
button.click()
