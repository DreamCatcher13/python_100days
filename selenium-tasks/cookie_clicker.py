from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
srvc = Service(r"C:\software\chromedriver.exe")

driver = webdriver.Chrome(service=srvc, options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, ('cookie'))
timeout = time.time() + 5  #setting the first 5 sec wait
store = driver.find_elements(By.CSS_SELECTOR, ('#store b'))
items = [ i.text for i in store]
all_prices = [int(i.split("-")[1].strip().replace(",", "")) for i in items[:-1]]

while True:
    cookie.click()

    if time.time() > timeout:   
        money = driver.find_element(By.ID, ('money')).text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)
        
        break

#okay selenium is not fun :(
        




