from plyer import notification
import requests
from bs4 import BeautifulSoup as bs
import os
import time

def notifyMe(title,message):
	notification.notify(
		title = title,
		message = message,
		app_icon = os.getcwd()+"\covid.ico",
		timeout = 15
		)

print("Welcome to the program.\n")
print("Do you wanna pop up the program in specific time intervals or one time?\n")
ask = int(input("enter 1 for one time or 2  for time interval: "))
ti_me = int(input("\nEnter the amount of interval in minutes which the program should pop up: "))
amount = ti_me*60

global total_case,total_death,total_rec
def getdata():
        r = requests.get("https://virusncov.com/")
        data = r.content
        soup = bs(data,'lxml')
        getdata.total_case = "Total Corona cases: %s " %(soup.h2.text.split(" ")[-1])+"\n"
        getdata.total_death = "Total Deaths: %s " %(soup.find("span",{"class":"red-text"}).text+"\n")
        getdata.total_rec = "Total Recovered: %s " %(soup.find("span",{"class":"green-text"}).text)
        

if ask == 1:
        print("\nfetching data\n")
        getdata()
        notifyMe("Corona stats",total_case+total_death+total_rec)
elif ask == 2:
        while True:
                getdata()
                notifyMe("Corona stats",getdata.total_case+getdata.total_death+getdata.total_rec)
                print("updating..")
                time.sleep(amount)
else:
        print("\nexiting")
        sys.exit()
