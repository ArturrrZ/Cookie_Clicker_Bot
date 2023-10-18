from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

opt=Options()
opt.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=opt)

driver.get('https://orteil.dashnet.org/experiments/cookie/')
time.sleep(1)

cookie=driver.find_element(By.XPATH,value='//*[@id="cookie"]')
items=driver.find_elements(By.CSS_SELECTOR,'#store div')
items_id=[item.get_attribute('id') for item in items]
timeout=time.time() + 5
#end of the game
five_minutes=time.time() + 60*5

end=False
while not end:
    cookie.click()
    if time.time() > timeout:
        end=True
        print('Game is ended')

driver.close()