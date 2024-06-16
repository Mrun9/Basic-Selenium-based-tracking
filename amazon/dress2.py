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

#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[*]//div/span/div/div/div[2]/div[2]/div[2]/h2/span'
#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/*/div/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span | //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/*/div/div/span/div/div/div[2]/div[2]/div/h2/span'
#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/*[div]//h2/span'
#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//*[div]/div/div/div/span/div/div/div[2]/div[2]/div[2]/h2/span'
#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/*[div]/*span/*[div]/*div[2]//h2/span'

#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//h2/span'

#xpath_pattern_company = '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]//h2/span'

name_company = 'a-size-base-plus a-color-base'
css_name = ".a-row.a-size-base.a-color-secondary"

x_name = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div"
x_name1 = "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]"

page_block = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, x_name1))
)[0]

company_divs = page_block.find_elements(By.CSS_SELECTOR, ".sg-col-4-of-24")

print(len(company_divs))

#exit()

companies = [div.text for div in company_divs]

for c in companies:
    print(f"Company: {c}")

print(f"Number of companies found : {len(companies)}")

time.sleep(5)
driver.quit()

# s-result-item s-widget s-widget-spacing-large AdHolder s-flex-full-width

# sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor
# sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor
# sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor
# sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20 gsx-ies-anchor