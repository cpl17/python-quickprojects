from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bot import InternetSpeedTwitterBot
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
SPEED_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login"

# User Info

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "#"
TWITTER_PASSWORD = "#"


driver = InternetSpeedTwitterBot(PATH)

driver.get_internet_speed(SPEED_URL)

driver.tweet_at_provider(TWITTER_URL)

