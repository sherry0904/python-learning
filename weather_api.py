import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 25.0333,
    "longitude": 121.5654,
    "current": "temperature_2m,apparent_temperature",
    "hourly": "precipitation_probability",
    "timezone": "Asia/Taipei"
}

def get_weather_data():
    try:

        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()


        print("API 呼叫失敗，狀態碼:", response.status_code)
        return {}

    except requests.RequestException:
        print("API 呼叫發生例外狀況")
        return {}


def get_weather_summary(data):
    temperature = data["current"]["temperature_2m"]
    apparent_temperature = data["current"]["apparent_temperature"]

    hourly_times = data["hourly"]["time"]
    rain_probabilities = data["hourly"]["precipitation_probability"]

    current_time = data["current"]["time"]
    current_hour = current_time[:13] + ":00"

    current_index = hourly_times.index(current_hour)
    current_rain_probability = rain_probabilities[current_index]

    return {
        "temperature": temperature,
        "apparent_temperature": apparent_temperature,
        "current_rain_probability": current_rain_probability
    }

data = get_weather_data()

if data: 
    summary = get_weather_summary(data)
    
    print("溫度:", summary["temperature"])
    print("體感溫度:", summary["apparent_temperature"])
    print("降雨機率:", summary["current_rain_probability"])
