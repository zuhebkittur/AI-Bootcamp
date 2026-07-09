import requests
from config import API_KEY

def get_weather(city):
    url = "https://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": city
    }

    try:
        response = requests.get(url, params=params)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Something went wrong!")
        print(e)
        return None