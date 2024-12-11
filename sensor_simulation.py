import requests
import random
import time

BASE_URL = "http://localhost:5000/data"

def simulate_sensor_data():
    payload = {
        "temperature": round(random.uniform(30.0, 50.0), 2),
        "humidity": round(random.uniform(10.0, 50.0), 2),
        "smoke_level": round(random.uniform(0.0, 10.0), 2),
        "co_level": round(random.uniform(0.0, 5.0), 2)
    }
    try:
        response = requests.post(BASE_URL, json=payload)
        print(f"Sent data: {payload}, Response: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")

while True:
    simulate_sensor_data()
    time.sleep(10)
