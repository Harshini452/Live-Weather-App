from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "5ad4854a72fc55fbf7135ffa2adbe7b7"  # Replace with your OpenWeatherMap API key

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            try:
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:
                    weather_data = {
                        "city": data["name"],
                        "temperature": f"{data['main']['temp']} °C",
                        "description": data["weather"][0]["description"].title(),
                        "humidity": f"{data['main']['humidity']}%",
                        "wind": f"{data['wind']['speed']} m/s"
                    }
                else:
                    error = data.get("message", "Failed to get data.")
            except Exception as e:
                error = str(e)
        else:
            error = "Please enter a city name."

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)
