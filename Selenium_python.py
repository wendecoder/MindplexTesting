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

button1 = driver.find_element(By.ID, "signup")
time.sleep(15)
button1.click()

popup1 = driver.find_element(By.ID, "signupModal")
assert popup1.is_displayed()
time.sleep(5)

closeModal1 = driver.find_element(By.ID, "close-signup")
closeModal1.click()
is_closed = closeModal1.is_displayed()
assert not is_closed

time.sleep(10)

button2 = driver.find_element(By.ID, "signin")
time.sleep(15)
button2.click()

popup2 = driver.find_element(By.ID, "signinModal")
assert popup2.is_displayed()
time.sleep(5)

closeModal2 = driver.find_element(By.ID, "close-signin")
closeModal2.click()
is_closed = closeModal2.is_displayed()
assert not is_closed
