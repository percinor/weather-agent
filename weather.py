from google import genai
from google.genai import types
import typing_extensions as typing
from google.colab import userdata
import datetime
GOOGLE_API_KEY= userdata.get('GOOGLE_API_KEY')

# return Citydate format
class Citydate(typing.TypedDict):
    cityname: str
    start_date: str
    end_date: str

def get_response(sprompt) -> Citydate:
 client = genai.Client(api_key=GOOGLE_API_KEY)
 response:Citydate = client.models.generate_content(
     model="gemini-2.0-flash",
     config=types.GenerateContentConfig(
        response_mime_type = "application/json",
        response_schema = Citydate,
     ),
     contents= sprompt )
 return response

Today = datetime.datetime.now().strftime("%Y-%m-%d")
print(Today)
Userinput = input("Your prompt: ")
Sysprompt = f""" You are a helpful assistant that extracts city, start date, and end date from user input.Today is {Today}

user's input: {Userinput}

**Instructions:**

1.  **Identify the City:**
    *   Locate the city name mentioned in the user's input.
    *   If the user's input does not contain a city name, default to "Shanghai".
    *   Ensure the city name in the output is formatted as "Shanghai" (or the identified city name, ensuring no spaces are included within the city name itself). If the identified city name *does* include spaces (e.g. "Los Angeles"), *remove* the spaces (e.g., "LosAngeles").

2.  **Identify the Dates:**
    *   Locate the start and end dates in the user's input. The date format is YYYY-MM-DD.
    *   **Date Keyword Handling:**
        *   If the user's input contains date-related keywords such as "today", "tomorrow", "yesterday", "next week", or similar phrases, **calculate the corresponding date(s)**. Use today as 2024-11-03.
        *   "Tomorrow" refers to the day after today.
        *   If only one date is provided (including keywords), assume it is both the start date and the end date.
    *   **Default Date:** If no date is provided in any form, default to today's date Today for both start_date and end_date. Use the format YYYY-MM-DD.

"""


# get cityname and location
import json
response = get_response(Sysprompt)
print(response.text)
city_data = json.loads(response.text)
cityname = city_data["cityname"]
start_date = city_data["start_date"]
end_date = city_data["end_date"]
print(city_data["cityname"])

from geopy.geocoders import Nominatim
from pprint import pprint
geolocator = Nominatim(user_agent="weather-app")
location = geolocator.geocode(cityname)
latitude=location.latitude
longitude=location.longitude
pprint(location)

import requests
# url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&start_date={start_date}&end_date={end_date}"
url = f"https://api.open-meteo.com/v1/forecast?daily=weather_code,apparent_temperature_max,apparent_temperature_min&latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}"
print(url)
res = requests.get(url)
data = res.json()
print(data['daily'])
