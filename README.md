# weather-agent
a python weather gemini agent

client.models.generate_content(
      model="gemini-2.0-flash",      
      contents= prompt )

What's tomorrow's date? What will the weather be like in Tokyo tomorrow?

give me a system prompt, extract information from user input to get city and start date and end date ,if only have a date ,start date and end date is same date. output a json

What will the weather be like in kyoto next Monday?



Sysprompt = f""" You are a helpful assistant that extracts city, start date, and end date information from user input. Today's date is: {Today} 
**Instructions:** 
If the user provides a single date, assume it's both the start and end date. The date format should be YYYY-MM-DD.
If the user provides a range of dates, extract the start and end dates accordingly. 
If no city is provided, return Halifax. The city format should be Losangels.
If no dates are provided, return today's date.
Output a JSON object containing the extracted information with the following keys: "city", "start_date", and "end_date".  
User input:
"""


#https://api.open-meteo.com/v1/forecast?daily=weather_code,apparent_temperature_max,apparent_temperature_min&latitude=35.0115754&longitude=135.7681441&start_date=2025-04-21&end_date=2025-04-21

#url = f"https://api.open-meteo.com/v1/forecast?daily=weather_code,apparent_temperature_max,apparent_temperature_min&latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}"


