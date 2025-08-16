from flask import Flask, render_template, request
from weather_service import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            weather_data = get_weather(city)
            if weather_data:
                weather = weather_data
            else:
                error = "City not found or API error"
    
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)
