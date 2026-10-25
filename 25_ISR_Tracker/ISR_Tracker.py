#Import modules
import requests
import datetime as dt
import smtplib
import time

#Set Email Id and Password
my_email="sender_email@gmail.com"
my_password="your_password"

#Get currebt time
time_now=dt.datetime.now()
current_hrs=time_now.hour #Get current Hours

#Our location 
my_lat=19.909464
my_lng=73.227110

#Get ISS current location
def is_iss_near():
    responce=requests.get(url="http://api.open-notify.org/iss-now.json") #Connect with iss api
    responce.raise_for_status() #Rise error if not connect

    data=responce.json() #Get data in JSON format

    latitude=float(data['iss_position']['latitude']) #Get ISS Latitude position
    longitude=float(data['iss_position']['longitude']) #Get ISS Longitude position
    
    #Check the ISS position is near our position or not 
    if (my_lat-5 <= latitude <= my_lat+5) and (my_lng-5 <= longitude <= my_lng+5):
        return True #If yes return TRUE

#Check is Night or not
def is_night():
    #Set our position Parameters
    parameters={
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0
    }
    
    resp=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters) #Connect with sunrise-sunset api
    resp.raise_for_status() #Rise error if not connect

    resp_data=resp.json() #Get data in JSON format

    sunrise=resp_data["results"]["sunrise"].split("T")[1].split(":")[0] #Get Sunrise time in Hours
    sunset=resp_data["results"]["sunset"].split("T")[1].split(":")[0] #Get Sunset time in Hours

    india_sunrise=int(sunrise)+5 #Convert sunrise time into india's sunrise time
    india_sunset=int(sunset)+5 #Convert sunset time into india's sunset time

    #Check is Night or not
    if current_hrs>=india_sunset or current_hrs<=india_sunrise:
        return True #If yes return TRUE

while True:
    if is_iss_near() and is_night(): #Check the ISS is near us or not and it Night time or not
        #Set Connection 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=my_password) #login in your Account
            #Send Email
            connection.sendmail(
                            from_addr=my_email, #Sender email id
                            to_addrs="receiver_email@gmail.com", #Receiver email id
                            msg="Subject:Look UP in SKY.\n\n The ISS is above You." #Message
                            )
    time.sleep(60) #Wait for 60 seconds