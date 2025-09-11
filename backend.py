from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "✅ Backend is running!"

# Tank endpoint (dummy data for now)
@app.route("/tank")
def tank():
    data = {
        "tank_id": 1,
        "level": 75.3,   # percentage
        "volume": 1500,  # liters
        "status": "OK"
    }
    return jsonify(data)

# Alerts endpoint (dummy alerts for now)
@app.route("/alerts")
def alerts():
    alerts_data = [
        {"id": 1, "message": "Low fuel warning", "level": "warning"},
        {"id": 2, "message": "Possible variance detected", "level": "critical"}
    ]
    return jsonify(alerts_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

