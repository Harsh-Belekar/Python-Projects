#Imports Modules
import requests
from twilio.rest import Client 

#Constants for weather API
weather_api="https://api.openweathermap.org/data/2.5/forecast"
api_key="your_API_Key"

#Constants for twilio API
account_SID="your_account_SID"
auth_token="your_auth_token"

#Parameters for weather API
weather_parms={
    "lat":19.909464,
    "lon":73.227110,
    "appid":api_key,
    "cnt":4
}

#Connect with weather API
responce=requests.get(url=weather_api,params=weather_parms)
responce.raise_for_status()

weather_data=responce.json() #Get data from weather API

will_rain=False
#Check there will be rain or not
for hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if 500 <= int(condition_code) <= 600:
        will_rain=True

#If there will be rain today
if will_rain:
    client=Client(account_SID,auth_token) #Connect with twilio API
    
    #Create message
    message= client.messages\
            .create(
                body="It's going to be rain today, Remember to bring an Umbrella ☔", #Alert Message
                from_="+12696262523", #Twilio sender number
                to="+91 your_number" #Receiver Number
            )

