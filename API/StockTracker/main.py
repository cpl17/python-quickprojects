import os
from dotenv import load_dotenv
import requests 
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

alpha_api_key = os.getenv("ALPHA_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
sms_api_key = os.getenv("SMS_API_KEY")


account_sid = "AC4861eebc683aecd86aa36599e7d3ef6b"
auth_token = "fc1e4687d20e2f639810ef5dcd0b7a43"


# Function for getting news 

def get_news():

    news_params = {

        'qInTitle': COMPANY_NAME,
        'pageSize': 3,
        'sortBy': "popularity",
        'apiKey': news_api_key 

    } 

    response = requests.get(url = NEWS_ENDPOINT, params=news_params)
    data = response.json()['articles']
    top3 = {article['title']:article['description'] for article in data}
    
    return top3 


# Get Stock Data

alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alpha_api_key
}

response = requests.get(url = ALPHA_ENDPOINT, params=alpha_params)
stock_data = response.json()["Time Series (Daily)"]

# Determine if there is a fluctuation 

close_price = float(stock_data["2021-01-08"]['4. close'])
previous_close_price  = float(stock_data["2021-01-07"]['4. close'])
percent_diff = round((((close_price - previous_close_price) /  previous_close_price) * 100),2)

high_fluctuation = percent_diff > 5

# Dealing with formatting the message 

body_text= """

TESLA: {}{}%
HEADLINE:{}
BRIEF: {}
"""

if percent_diff > 0:
    chg_symbol = "🔺"
else:
    chg_symbol = "🔺"


if high_fluctuation:
    
    top3 = get_news()

    client = Client(account_sid, auth_token)

    for title,description in top3.items():
        message = client.messages \
                    .create(
                        body=body_text.format(chg_symbol,percent_diff,title,description),
                        from_='+15154686216',
                        to='+13028240859'
                )
   






    
    



















#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

