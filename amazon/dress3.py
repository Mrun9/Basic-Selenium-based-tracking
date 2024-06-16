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

xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//h2/span'

company_divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath_pattern_company))
)

companies = [div.text for div in company_divs]

xpath_pattern_product = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//div[2]/h2'

product_divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath_pattern_product))
)

products = [div.text for div in product_divs]

final = list(zip(companies, products))

for c, p in final:
    print(f"Company: {c}, Product: {p}")

print(f"Number of companies found : {len(companies)}")
print(f"Number of companies found : {len(products)}")

time.sleep(100)
driver.quit()