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

driver.get("http://172.16.10.2/movies/pirates-of-the-caribbean-dead-men-tell-no-tales/")

link = driver.find_element_by_partial_link_text('DOWNLOAD')
link.click()
