import requests


with open("apikey.txt", "r") as f:
    key = f.read().strip()

parameters = {
    "lat": 48.6223732,
    "lon": 22.3022569,
    "appid": key,
    "cnt": 8,
    "units": "metric",
}

responce = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
responce.raise_for_status()
weather_data = responce.json()
for i in range(0,parameters['cnt']):
    if weather_data['list'][i]['weather'][0]['id'] < 700:
        print("Bring an umbrella")
        print(weather_data['list'][i]['weather'][0]['description'])
        print(weather_data['list'][i]['dt_txt'] + ' UTC')