#this code pulls from the free api openweather and displays the current temperature for the zip code answered - in this case Hermosa Beach, CA

import requests

zip_code = "90254"
api_key = "api"
url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&units=imperial&appid={api_key}"

response = requests.get(url)
weather_data = response.json()

current_temperature = weather_data["main"]["temp"]
daily_high = weather_data["main"]["temp_max"]
daily_low = weather_data["main"]["temp_min"]
weather_condition = weather_data["weather"][0]["description"]

print(f"The current temperature in {zip_code} is {current_temperature} degrees Fahrenheit.")
print(f"The daily high for today is {daily_high} degrees Fahrenheit.")
print(f"The daily low for today is {daily_low} degrees Fahrenheit.")
print(f"The current weather condition is {weather_condition}.")
