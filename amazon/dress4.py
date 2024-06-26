from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time 

# Setup ChromeDriver with user agent and options
options = Options()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
serv = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=serv, options=options)

# Open Amazon
driver.get("https://www.amazon.com/")

# Wait for the search box to be present and perform the search
search_box = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='twotabsearchtextbox']"))
)
search_box.clear()
search_box.send_keys("women summer dresses" + Keys.ENTER)

# Wait for the search results to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@data-component-type='s-search-results']"))
)

# Scroll and load more results
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for the page to load
    
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Extract the parent elements that contain both product name and company name
product_containers = driver.find_elements(By.XPATH, "//div[contains(@data-component-type, 's-search-result')]")

# Extract product names and company names together
products_companies = []
for container in product_containers:
    try:
        product_name = container.find_element(By.XPATH, ".//span[contains(@class, 'a-size-base-plus a-color-base a-text-normal')]").text.strip()
    except:
        product_name = ""
    try:
        company_name = container.find_element(By.XPATH, ".//span[contains(@class, 'a-size-base-plus a-color-base')]").text.strip()
    except:
        company_name = ""
    
    products_companies.append((product_name, company_name))

# Print the product names and company names
for product, company in products_companies:
    print(f"Product: {product} | Company: {company}")

# Write the product names and company names to a CSV file
with open('amazon_dress.tsv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(["Product Name", "Company Name"])  # Write the header
    writer.writerows(products_companies)  # Write the data

# Clean up
time.sleep(5)
driver.quit()
