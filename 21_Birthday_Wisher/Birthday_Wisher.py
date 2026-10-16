#Import modules
import pandas
import smtplib
import datetime as dt
import random

#Set Email Id and Password
my_email="your_email@gmail.com"
my_password="your_password"

#Get Current Date
today=dt.datetime.now()
today_date=(today.month,today.day) #Get current month & day

#Take data from csv file
data=pandas.read_csv("./Assets/brithdays.csv")

#Insert data into brithday dictionary
brithday_dic={ (row["month"],row["day"]) : row for (index,row) in data.iterrows()}

#Check the brithday date match the current day or not
if today_date in brithday_dic:
    brithday_person=brithday_dic[today_date] #Get Brithday person 
    file_path=f"./Assets//letter_{random.randint(1,3)}.txt"
    with open(file=file_path,mode="r") as f:
        content=f.read()
        content=content.replace("[NAME]",brithday_person["name"])

    #Set Connection 
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password) #login in your Account
        #Send Email
        connection.sendmail(
                        from_addr=my_email,
                        to_addrs=brithday_person["email"],
                        msg=f"Subject:Happy Brithday Wishes.\n\n{content}"
                        )