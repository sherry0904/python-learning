import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 25.0333,
    "longitude": 121.5654,
    "current": "temperature_2m,apparent_temperature",
    "hourly": "precipitation_probability",
    "timezone": "Asia/Taipei"
}

data = {}

try:

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
    else:
        print("API 呼叫失敗，狀態碼:", response.status_code)

except requests.RequestException:
    print("API 呼叫發生例外狀況")

if data:
    temperature = data["current"]["temperature_2m"]
    apparent_temperature = data["current"]["apparent_temperature"]

    hourly_times = data["hourly"]["time"]
    rain_probabilities = data["hourly"]["precipitation_probability"]

    current_time = data["current"]["time"]
    current_hour = current_time[:13] + ":00"

    current_index = hourly_times.index(current_hour)

    current_rain_probability = rain_probabilities[current_index]

    print("溫度", temperature)
    print("體感溫度", apparent_temperature)
    print("降雨機率:", current_rain_probability)
