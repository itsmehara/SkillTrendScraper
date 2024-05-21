from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service

import pandas as pd
import time


service = Service(executable_path=r"/opt/homebrew/bin/chromedriver")
options = webdriver.ChromeOptions()
#browser = webdriver.Chrome(executable_path=r"/opt/homebrew/bin/chromedriver")
browser = webdriver.Chrome(service=service, options=options)

browser.get("https://www.naukri.com")

wd_search_box_xpath = r'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input'
wd_search_button_xpath = r'//*[@id="root"]/div[7]/div/div/div[6]'
input_search = browser.find_element(By.XPATH, wd_search_box_xpath)
input_search.send_keys("AWS Architect")

button_search = browser.find_element(By.XPATH, wd_search_button_xpath).click()

val = input("enter value 100:")
# time.sleep(9000)

browser.quit()

