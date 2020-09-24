from selenium import webdriver as WD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

# setting up  driver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = WD.Chrome(PATH)

# setting up targeted website

# driver.get("https://www.python.org/")
driver.get("http://2.2.2.2/")

# fun begins
print(driver.title)

# do some fun with search box
# search = driver.find_element_by_id("id-search-field")
search = driver.find_element_by_id("s")
search.send_keys("pirates")   
search.send_keys(Keys.RETURN)
# print(driver.page_source)

# getting info from the search page

try:
    info = WDW(driver,5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'title')))
except:
    driver.quit()

# print(info.text)
for i in info:
    print(i.text)

time.sleep(5)
driver.quit()

