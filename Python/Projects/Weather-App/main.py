import requests
# API_KEY = "900ad0f2f43b4a2bbaf132420260607"

# def display_weather(data):
#         print("=" * 40)
#         print("🌦️ WEATHER REPORT")
#         print("=" * 40)
#         print(f"📍 City        : {data['location']['name']}")
#         print(f"🏙️ Region      : {data['location']['region']}")
#         print(f"🌍 Country     : {data['location']['country']}")
#         print(f"🌡️ Temperature : {data['current']['temp_c']} °C")
#         print(f"💧 Humidity    : {data['current']['humidity']} %")
#         print(f"💨 Wind Speed  : {data['current']['wind_kph']} km/h")
#         print(f"☁️ Condition   : {data['current']['condition']['text']}")
#         print("=" * 40)

# def get_weather(city):
#     url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
#     response = requests.get(url)
#     data = response.json()
#     return data

from weather import get_weather
from display import display_weather

def main():
    city = input("Enter the city: ")
    data = get_weather(city)

    if "error" in data:
        print(data["error"]["message"])
    else:
        display_weather(data)

if __name__ == "__main__":
    main()
    