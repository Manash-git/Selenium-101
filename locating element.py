from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time

# setting up  driver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = wd.Chrome(PATH)

# setting up targeted website

# driver.get("https://www.python.org/")
driver.get("http://2.2.2.2/")



# fun begins
print(driver.title)

# do some fun with search box
# search = driver.find_element_by_id("id-search-field")
search = driver.find_element_by_id("s")
# search = driver.find_element_by_class_name('search-box')
search.send_keys("pirates")   
search.send_keys(Keys.RETURN)
# print(driver.page_source)

# for loading the seacrh page need some time
time.sleep(5)


driver.quit()

