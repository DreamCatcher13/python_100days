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
# driver.get("https://www.python.org/")

# lis = driver.find_elements(By.CSS_SELECTOR, ('.event-widget li'))
# my_dict = {}
# for l in range(len(lis)):
#     li = lis[l]
#     time = li.find_element(By.TAG_NAME, ("time")).text
#     event = li.find_element(By.TAG_NAME, ("a")).text
#     temp = {
#         'time': time,
#         'event': event
#     }
#     my_dict[str(l)] = temp
# #driver.close() # tab
# print(my_dict)
# driver.quit()  # all browser

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_elements(By.CSS_SELECTOR, ('#articlecount a'))[0]
article_count.click()
wiki_quote = driver.find_element(By.LINK_TEXT, ("Wikibooks"))
wiki_quote.click()
search = driver.find_element(By.NAME, ("search"))
search.send_keys("Python")
search.send_keys(Keys.ENTER)


#print(article_count)
#driver.quit()