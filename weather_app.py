import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'City': data['name'],
                'Temperature': f"{data['main']['temp']} °C",
                'Weather': data['weather'][0]['description'].title(),
                'Humidity': f"{data['main']['humidity']}%",
                'Wind Speed': f"{data['wind']['speed']} m/s"
            }
            return weather
        else:
            return f"Error: {data.get('message', 'Something went wrong')}"
    except requests.exceptions.RequestException as e:
        return f"Network Error: {e}"

def main():
    api_key = "5ad4854a72fc55fbf7135ffa2adbe7b7"  # Replace with your actual API key
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    result = get_weather(city, api_key)

    if isinstance(result, dict):
        print("\n=== Weather Details ===")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)

if __name__ == "__main__":
    main()
