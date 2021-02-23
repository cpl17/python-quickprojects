from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"

# User Info

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "#"
TWITTER_PASSWORD = "#"

class InternetSpeedTwitterBot():

    def __init__(self, driver_path): 
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = None
        self.up = None
    
    def get_internet_speed(self,url):
        
        self.driver.get(url)

        # Click the button
        button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        button.click()

        time.sleep(60)

        # Get download speeds

        self.down = float(self.driver.find_element_by_class_name("download-speed").text)
        self.up = float(self.driver.find_element_by_class_name("upload-speed").text)

        print(self.down)
        print(self.up)


    def tweet_at_provider(self,url):
        
        self.driver.get(url)

        time.sleep(5)

        # Login

        

        user_form = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user_form.send_keys(TWITTER_EMAIL)

        pwd = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pwd.send_keys(TWITTER_PASSWORD)

        time.sleep(2)
        pwd.send_keys(Keys.ENTER)


        # Tweet

        time.sleep(5)

        tweet_box = self.driver.find_element_by_class_name("public-DraftStyleDefault-block")
        tweet_box.send_keys(f"My upload speed is {self.up}. My download speed is {self.down}")

        time.sleep(2)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)

        self.driver.quit()






        

driver = InternetSpeedTwitterBot(PATH)

driver.get_internet_speed(SPEED_URL)

driver.tweet_at_provider(TWITTER_URL)

