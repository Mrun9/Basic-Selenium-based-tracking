from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import csv 
import time 

options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
serv = Service(
    executable_path="chromedriver.exe"
)

driver = webdriver.Chrome(service=serv,options=options)

driver.get("https://www.amazon.com/")

WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='twotabsearchtextbox']"))
)

input_element = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
input_element.clear()
input_element.send_keys("women summer dresses" + Keys.ENTER)

x_name1 = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]"
x_name2 = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]"

css_name = ".a-row.a-size-base.a-color-secondary"

page_block = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, x_name2))
)[0]

company_divs = page_block.find_elements(By.CSS_SELECTOR, ".a-text-normal.a-color-base")

companies = [div.text for div in company_divs]

for c in companies:
    print(f"Company: {c}")

##################################


price_divs = page_block.find_elements(By.CLASS_NAME, 'a-row.a-size-base.a-color-base')

prices = [div1.text for div1 in price_divs]

for p in prices:
    print(f"Price : {p}")


##################
print("Lenghts: ")
print(len(company_divs))
print(len(prices))

time.sleep(5)
driver.quit()
