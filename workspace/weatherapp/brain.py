import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_condition = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            rain_chance = data.get("rain", {}).get("1h", 0)

            result_dict = {
                'weather_condition' : data["weather"][0]["description"],
                'temperature' : data["main"]["temp"],
                'humidity' : data["main"]["humidity"],
                'rain_chance' : data.get("rain", {}).get("1h", 0)
            }

            return result_dict
        else:
            return f"Error: {data['message']}"

    except Exception as e:
        return f"An error occurred: {e}"


api_key = "37216b63a92c35f827dbea0f18e96b29"
# city = input("Enter the city name: ")

# result = get_weather(api_key, city)
# print(result)