from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# Wait for the "Next" button to be present and clickable
next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator'))
)

# Click the "Next" button
next_button.click()

# Wait for the new page to load
time.sleep(5)

# Close the WebDriver
driver.quit()
