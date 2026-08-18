forecast = [
    {
        "day": "Monday",
        "rain_probability": 20
    },
    {
        "day": "Tuesday",
        "rain_probability": 70
    },
    {
        "day": "Wednesday",
        "rain_probability": 40
    }
]

print(forecast[0]["day"])
print(forecast[1]["rain_probability"])
print(forecast[2]["rain_probability"]) 


rain_probability = 30
if rain_probability >= 50:
    print("記得帶傘")
else:
    print("今天不用帶傘")


rain_probability = 20
if rain_probability >= 70:
    print("一定要帶傘")
elif rain_probability >= 40:
    print("建議帶傘")
else:
    print("今天不用帶傘")

def get_umbrella_advice(rain_probability):
    if rain_probability >= 70:
        return "一定要帶傘"
    elif rain_probability >= 40:
        return "建議帶傘"
    else:
        return "今天不用帶傘"

for day_forecast in forecast:
    day = day_forecast["day"]
    rain_probability = day_forecast["rain_probability"]
    
    advice = get_umbrella_advice(rain_probability)
    
    print(f"{day}: {advice}")


def should_bring_umbrella(rain_probability):
    return rain_probability >= 50

print(should_bring_umbrella(70))
print(should_bring_umbrella(30))
