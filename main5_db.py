from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

serv = Service(
    executable_path="chromedriver.exe"
)

driver = webdriver.Chrome(service=serv)

driver.get("https://grubhubdrivershop.com/collections/shop-all")

# Wait for the divs with the product titles to be present
product_divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card__title"))
)

# Extract and store the text inside each div
products = [div.text for div in product_divs]

price_divs = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "price-item--regular"))
)

prices = [div.text for div in price_divs]

# Combine product names and prices together
final = list(zip(products, prices))

# Print them together
for t, p in final:
    print(f"Product: {t}, Price: {p}")

print(f"No of product prices found: {len(products)}")

# Create a DataFrame using pandas
df = pd.DataFrame(final, columns=["Product", "Price"])

# Print the DataFrame to see it in a table format
print(df)

# Optionally, save the DataFrame to a TSV file
df.to_csv('products.tsv', sep='\t', index=False)

time.sleep(20)
driver.quit()
