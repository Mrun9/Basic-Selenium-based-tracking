from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time 

serv = Service(
    executable_path="chromedriver.exe"
)

driver = webdriver.Chrome(service=serv)

driver.get("https://www.amazon.com/")

WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input"))
)

input_element = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
input_element.clear()
input_element.send_keys("women summer dresses" + Keys.ENTER)

time.sleep(500)
driver.quit()