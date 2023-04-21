from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdeALxVq7qnSc-V9tm97zfdIXMsM9lTr9AKqyaMhFwGtewRbQ/viewform?usp=sf_link"
SITE_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.88836615784793%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.662044543503555%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A398300%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

options = Options()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
srvc = Service(r"C:\software\chromedriver.exe")

driver = webdriver.Chrome(service=srvc, options=options)
driver.get(SITE_URL)
time.sleep(3)
all_apartments = driver.find_elements(By.CLASS_NAME, ('property-card-data'))
links = []
addr = []
price = []
for i in range(len(all_apartments)):
    links.append(all_apartments[i].find_element(By.TAG_NAME, ('a')).get_attribute('href'))
    addr.append(all_apartments[i].find_element(By.TAG_NAME, ('address')).text)
    price.append(all_apartments[i].find_element(By.TAG_NAME, ('span')).text)

print(price)
print(links)
print(addr)

driver.quit()


