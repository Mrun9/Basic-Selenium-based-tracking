from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

service = Service(
    executable_path="chromedriver.exe"
)

driver = webdriver.Chrome(service=service)

driver.get("https://grubhubdrivershop.com/collections/shop-all")



#This clicks the bottle image on grubhub and opens the linked page


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "ProductCardImage-collection-template-4327953006637"))
)

link = driver.find_element(By.ID, "ProductCardImage-collection-template-4327953006637")
link.click()

time.sleep(20)

driver.quit()
