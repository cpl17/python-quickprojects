from bs4 import BeautifulSoup
import requests 
import lxml


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

PATH = "C:\Program Files (x86)\chromedriver.exe"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLScpxZX8YF_y0az8InbUgJypcOXlYa4A-1L1vTiXeJqIxP-O2Q/viewform?usp=sf_link"


# Scrape all the lists from the provided path 


headers = {

    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Chrome/87.0.4280.141"
}

response = requests.get(URL, headers = headers)
renting_page = response.text

soup = BeautifulSoup(renting_page,"lxml")


# Create a list of all the links 

elements = soup.find_all(name = "a", class_ = "list-card-link", attrs={"tabindex":"0"})

links = ["https://www.zillow.com/" + element['href'] for element in elements]



# Create a list of prices for all the listings  

elements = soup.find_all(name = "div", class_ = "list-card-price")

def format_price(price):
    price = int(price.strip("$+mo/").split()[0].replace(",","").replace("+",""))
    return price

prices = [format_price(element.text) for element in elements]



# Create a lists of address for all the listings you scraped 


elements = soup.find_all(name = "address", class_ = "list-card-addr")

addresses = [element.text for element in elements]



# Use Selenium to fill in the form # 



driver = webdriver.Chrome(executable_path=PATH)
driver.get(FORM_URL)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "exportFormTitle"))
)



for tup in list(zip(addresses,prices,links)):

    num = 1

    for entry in tup:
    
        obj = driver.find_element_by_css_selector(f"input[aria-labelledby='i{num}']")
        obj.click()
        obj.send_keys(entry)
        num +=4

    driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Submit another response"))
        )

    driver.find_element_by_link_text("Submit another response").click()


        



 





