import json

def get_umbrella_advice(rain_probability):
    if rain_probability >= 70:
        return "一定要帶傘"
    elif rain_probability >= 40:
        return "建議帶傘"
    else:
        return "今天不用帶傘"

try: 
    with open("data/weather.json", "r", encoding="utf-8") as file:
        forecast = json.load(file)
except FileNotFoundError:
    print("找不到檔案")
except json.JSONDecodeError:
    print("JSON 格式錯誤")

for day_forecast in forecast:
    day = day_forecast["day"]
    rain_probability = day_forecast["rain_probability"]
    
    advice = get_umbrella_advice(rain_probability)
    
    print(f"{day}: {advice}")

for day_forecast in forecast:
    day = day_forecast["day"]
    rain_probability = day_forecast["rain_probability"]
    
    advice = get_umbrella_advice(rain_probability)
    
    print(f"{day}: {advice}")

def should_bring_umbrella(rain_probability):
    return rain_probability >= 50


print(should_bring_umbrella(70))
print(should_bring_umbrella(30))


