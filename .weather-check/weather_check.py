import os
import requests
import datetime

# Weather config
API_KEY = os.environ['OWM_API_KEY']
ZIP = os.environ['ZIP']
RAIN_THRESHOLD = 0.05

# Telegram config
BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    print(f"Telegram API response: {response.status_code} - {response.text}")

# Weather logic
url = f"https://api.openweathermap.org/data/2.5/forecast?zip={ZIP},US&appid={API_KEY}&units=imperial"
response = requests.get(url)
data = response.json()
print(data)

now = datetime.datetime.utcnow()
cutoff = now + datetime.timedelta(hours=12)
rain_expected = 0.0

for entry in data['list']:
    forecast_time = datetime.datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
    if now < forecast_time <= cutoff:
        rain_mm = entry.get('rain', {}).get('3h', 0)
        rain_in = rain_mm * 0.0393701
        rain_expected += rain_in

msg = ""

if rain_expected >= RAIN_THRESHOLD:
    msg = f"🌧️ Rain expected in next 12 hours ({rain_expected:.2f}\"), skip watering."
else:
    msg = "🟢 No rain expected. Water as planned."

print(msg)

# Send Telegram message
try:
    send_telegram_message(msg)
    print("✅ Telegram message sent (attempted)")
except Exception as e:
    print(f"❌ Failed to send Telegram message: {e}")

