import os
import requests
import datetime

API_KEY = os.environ['OWM_API_KEY']
LAT = os.environ['LATITUDE']
LON = os.environ['LONGITUDE']
RAIN_THRESHOLD = 0.05  # inches (can adjust as needed)

url = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units=imperial"

response = requests.get(url)
data = response.json()

now = datetime.datetime.utcnow()
cutoff = now + datetime.timedelta(hours=12)
rain_expected = 0.0

for entry in data['list']:
    forecast_time = datetime.datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
    if now < forecast_time <= cutoff:
        rain = entry.get('rain', {}).get('3h', 0)
        rain_expected += rain

if rain_expected >= RAIN_THRESHOLD:
    print(f"🌧️ Rain expected in next 12 hours ({rain_expected:.2f}\"), skip watering.")
else:
    print("🟢 No rain expected. Water as planned.")
