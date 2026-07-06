import requests
API_KEY = "900ad0f2f43b4a2bbaf132420260607"
city = input("Enter the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
response = requests.get(url)
data = response.json()

if "location" in data:
    print("=" * 40)
    print("🌦️ WEATHER REPORT")
    print("=" * 40)
    print(f"📍 City        : {data['location']['name']}")
    print(f"🏙️ Region      : {data['location']['region']}")
    print(f"🌍 Country     : {data['location']['country']}")
    print(f"🌡️ Temperature : {data['current']['temp_c']} °C")
    print(f"💧 Humidity    : {data['current']['humidity']} %")
    print(f"💨 Wind Speed  : {data['current']['wind_kph']} km/h")
    print(f"☁️ Condition   : {data['current']['condition']['text']}")
    print("=" * 40)
else:
    print(data["error"]["message"])