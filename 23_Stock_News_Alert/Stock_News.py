#Import modules
import requests
from twilio.rest import Client 

#Constants
STOCK_NAME="IBM"
COMPANY_NAME="IBM India Private Limited"

#Constants for twilio API
account_SID="your_account_SID"
auth_token="your_auth_token"

#Api Keys
stock_aip_key="your_stock_API_Key"
news_api_key="your_news_API_Key"

#Api endpoints
stock_endpoint="https://www.alphavantage.co/query"
news_endpoint="https://newsapi.org/v2/everything"

#Stock parameters
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":stock_aip_key
}

stock_responce=requests.get(url=stock_endpoint,params=stock_params) #Connect to stock api
data=stock_responce.json()["Time Series (Daily)"] #Get speciffic data
data_list=[value for (key,value) in data.items()] #Get specific value from data

#Get yesterdays stock closing price
yesterday_data=data_list[0]
yesterday_closing_price=float(yesterday_data['4. close'])

#Get day before yesterdays stock closing price
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing=float(yesterday_data['4. close'])

up_down=None
difference=yesterday_closing_price-day_before_yesterday_closing #Difference between stock price
if difference >0:
    up_down="🔼"
else:
    up_down="🔻"

diff_percent=round((difference/yesterday_closing_price)*100) #Get percentage of Difference in stock

#If percentage is greather then 5
if abs(diff_percent) > 5:
    news_params={
            "q":COMPANY_NAME,
            "apikey":news_api_key
    }

    news_responce=requests.get(url=news_endpoint,params=news_params) #Connect to news api
    articles=news_responce.json()['articles'] #Get speciffic data
    three_articles=articles[:3] #Get letest 3 articles

    #Make and orginize message for sending
    formated_article=[f"{STOCK_NAME}:{up_down} {diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client=Client(account_SID,auth_token) #Connect with twilio API

    for news in formated_article:
        #Create message
        message= client.messages\
                .create(
                    body=news, #Alert Message
                    from_="+12696262523", #Twilio sender number
                    to="+91 your_number" #Receiver Number
                )