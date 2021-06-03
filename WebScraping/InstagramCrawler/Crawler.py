from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

import time



class InstaFollower():

    def __init__(self,driver_path):

        self.driver = webdriver.Chrome(executable_path=driver_path)
    
    def login(self,url):

        self.driver.get(url)


        # Login Page

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        self.driver.find_element_by_name("username").send_keys(USERNAME)
        
        element = self.driver.find_element_by_name("password")
        element.send_keys(PASSWORD)
        element.send_keys(Keys.ENTER)

        # Dialog Boxes

        time.sleep(3)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        time.sleep(3)

        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()


    
    def find_followers(self):

        # Search for user

        time.sleep(3)

        element = self.driver.find_element_by_css_selector("input[placeholder = 'Search'")
        element.send_keys(SIMILAR_ACCOUNT)

        time.sleep(3)
        element.send_keys(Keys.ENTER)
        element.send_keys(Keys.ENTER)


        # Open followers page 

        time.sleep(3)

        element = self.driver.find_element_by_css_selector(f"a[href = '/{SIMILAR_ACCOUNT}/followers/']")
        element.click()

        time.sleep(3)

        # Get full screen page 

        scr = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

        for i in range(10):
            
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr)
            time.sleep(2)


    def follow(self):
        
        
        while True:
       
            # Get scroll height
            
            all_buttons = self.driver.find_elements_by_css_selector("li button")
            

            for button in all_buttons:

                try:

                    button.click()
                    time.sleep(.5)

                except ElementClickInterceptedException:

                    cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                    cancel_button.click()
                    time.sleep(.5)

                except StaleElementReferenceException:
            
                    # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", scr)
                    pass
