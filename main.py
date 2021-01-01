# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pyttsx3
import requests
import time
from datetime import datetime
engine = pyttsx3.init()
BASE_URL = "https://api.weatherapi.com/v1/forecast.json?"
API_KEY = "<API_KEY>"
CITY = "Seattle"
INTERVAL = 30

def say_text(text):
    # Use a breakpoint in the code line below to debug your script.
    engine.say(text)
    engine.runAndWait()

def get_weatherdata(city):
    hour = datetime.now().hour
    resp = requests.get(BASE_URL+"key="+API_KEY+"&q="+city+"&hour="+str(hour))
    weather_object = resp.json()
    current_weather = weather_object["current"]
    say_text("Current Weather")
    annouce_current_weather(current_weather)
    forecast = weather_object["forecast"]
    todays_forecast = forecast["forecastday"][0]
    next_hour_forecast = todays_forecast["hour"][0]
    say_text("Weather forecast for next hour")
    announce_forecast(next_hour_forecast)
    
def annouce_current_weather(current_weather):
	say_text("Temperature outside is "+str(current_weather["temp_f"])+" degrees fahrenheit.")
	if "condition" in current_weather.keys():
		say_text("Condition outside: "+current_weather["condition"]["text"])

def announce_forecast(next_hour_weather):
	say_text("Temperature outside will be "+str(next_hour_weather["temp_f"])+" degrees fahrenheit.")
	if "condition" in next_hour_weather.keys():
		say_text("Condition for next hour: "+next_hour_weather["condition"]["text"])

while True:
	get_weatherdata(CITY)
	time.sleep(INTERVAL)
