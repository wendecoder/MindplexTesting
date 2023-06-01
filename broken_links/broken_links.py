from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://magazine.mindplex.ai/the-politics-of-appropriation-and-the-active-use-of-content-creating-ai/")

# time.sleep(10)
links = driver.find_elements(By.CSS_SELECTOR, "a")
for link in links:
    url = link.get_attribute("href")
    if url != None:
        result = requests.head(url)

        if result.status_code != 200:
            print(Fore.RED+url, Fore.MAGENTA+str(result.status_code))