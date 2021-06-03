from Crawler import InstaFollower()



PATH = "C:\Program Files (x86)\chromedriver.exe"

SIMILAR_ACCOUNT = 'kruispunt4.0'
USERNAME = '#'
PASSWORD = '#'

INSTAURL = "https://www.instagram.com/accounts/login/"


# Login and follow accounts of provided account

follower = InstaFollower(PATH)

follower.login(INSTAURL)

follower.find_followers()

follower.follow()
