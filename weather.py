from google import genai
from google.genai import types
import typing_extensions as typing
from google.colab import userdata

GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

import json
def Genres(prompt:str):
 response = client.models.generate_content(
      model="gemini-2.0-flash",
      config= types.GenerateContentConfig(
          response_mime_type="application/json",
          response_schema=Citydate              
      ),
      contents= prompt )
 res = json.loads(response.text)
 return res
class Citydate(typing.TypedDict):
    city: str
    start_date: str
    end_date: str
    
#  set Sysprompt from question  extracts city, start date, and end date information from user input.
import datetime
Today = datetime.date.today().strftime("%Y-%m-%d")
Sysprompt = f""" You are a helpful assistant that extracts city, start date, and end date information from user input. Today's date is: {Today} 
**Instructions:** 
If the user provides a single date, assume it's both the start and end date. The date format should be YYYY-MM-DD.
If the user provides a range of dates, extract the start and end dates accordingly. 
If no city is provided, return Halifax. The city format should be Losangels.
If no dates are provided, return today's date.
User input:
"""
# Userinput = input("Your question")
Sysprompt = Sysprompt + "What will the weather be like in kyoto next Monday?"

cityjson = Genres(Sysprompt)
print(cityjson)

# get latitude and longitude from city
from geopy.geocoders import Nominatim
from pprint import pprint
geolocator = Nominatim(user_agent="weather-app")
location = geolocator.geocode(cityjson["city"])
pprint(location)
latitude=location.latitude
longitude=location.longitude
start_date = cityjson["start_date"]
end_date = cityjson["end_date"]
#  get weather
url = f"https://api.open-meteo.com/v1/forecast?daily=weather_code,apparent_temperature_max,apparent_temperature_min&latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}"
print(url)
import requests
wheater = requests.get(url).json()
print(wheater["daily"])
