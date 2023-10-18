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
for _ in range(1000):

    cookie.click()