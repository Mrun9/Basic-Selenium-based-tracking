from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://grubhubdrivershop.com/collections/shop-all")

# Wait for the divs with the product titles to be present
product_title_divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card__title"))
)

# Extract and store the text inside each div
products = [div.text for div in product_title_divs]

# Print the list of product titles
for product in products:
    print(product)

# Get and print the length of the products list
print(f"Number of products found: {len(products)}")

# Optionally wait a bit before closing the driver
time.sleep(20)

driver.quit()
