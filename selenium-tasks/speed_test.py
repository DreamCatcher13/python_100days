from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class InternetSpeedTestBot:
    def __init__ (self, service_path):
        
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.srvc = Service(service_path)
        self.driver = webdriver.Chrome(service=self.srvc, options=self.options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        accept_button = self.driver.find_element(By.ID, ("onetrust-accept-btn-handler"))
        accept_button.click()
        time.sleep(3)
        go_button = self.driver.find_element(By.CSS_SELECTOR, (".start-button a"))
        go_button.click()
        time.sleep(120)
        down = self.driver.find_element(By.CLASS_NAME, ("download-speed")).text
        up = self.driver.find_element(By.CLASS_NAME, ("upload-speed")).text
        print(f"Your download speed is {down} mb/s, your upload speed is {up} mb/s")


srvc_path = "C:\software\chromedriver.exe"
bot = InternetSpeedTestBot(service_path=srvc_path)
bot.get_internet_speed()