from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Moscow"):
    API_KEY = '87ec0d336a612bb69196272ffea83901'
    CITY_NAME = 'Moscow'
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={CITY_NAME}&units=imperial'
    response = requests.get(request_url)

    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: {response.status_code}")

    weather_data = response.json()
    return weather_data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Moscow"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)