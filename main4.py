from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

serv = Service(
    executable_path="chromedriver.exe"
)

driver = webdriver.Chrome(service=serv)

driver.get("https://grubhubdrivershop.com/collections/shop-all")

price_divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price-item--regular"))
)

prices = [div.text for div in price_divs]

for p in prices:
    print(p)

print(f"No of product prices found: {len(prices)}")

time.sleep(20)

driver.quit()