from selenium import webdriver as WD
from selenium.webdriver.common.action_chains import ActionChains as AC 


# setting up  driver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = WD.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker/')

driver.implicitly_wait(10)  # for initial loading

click_element = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')

action = AC(driver)
action.click(click_element)

buy_item = [driver.find_element_by_id('productPrice' + str(i)) for i in range(1,-1,-1)]   # takes first 2 in reverse order => [100,15]
for i in buy_item:
    print(i.text)

for i in range(100):
    action.perform()
    # print(cookie_count.text)
    count = int(cookie_count.text.split(" ")[0])
    # print(count)
    for j in buy_item:
        which_item = int(j.text)
        
        if count >= which_item:
            do_buy = AC(driver)
            
            do_buy.move_to_element(j)
            do_buy.click()
            do_buy.perform()