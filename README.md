# WeatherCheck 🌦️

A GitHub Actions automation that checks the weather forecast for your ZIP code using the OpenWeatherMap API and sends a Telegram message if rain is expected. Ideal for automating irrigation decisions — especially useful when seeding new grass!

---

## ✅ What It Does

- Checks the 5-day forecast for your ZIP code
- Sums expected rainfall (in inches) over the next 12 hours
- If rainfall exceeds a defined threshold, sends a Telegram alert advising to **skip watering**

---

## 🧱 Tech Stack

- Python 3.11
- OpenWeatherMap API (`/forecast` endpoint)
- GitHub Actions (CI/CD scheduling)
- Telegram Bot API (push notifications)

---

## ⚙️ Setup Instructions

### 1. 🍴 Fork or Clone this Repository

```bash
git clone https://github.com/ShezzyBear/WeatherCheck.git
```

### 2. 🔐 Add Secrets to GitHub Actions
Go to: Settings > Secrets > Actions in your repo and add the following:

| Secret Name | Example Value | Description |
|-------------|---------------|-------------|
| `OWM_API_KEY` | `abc123...` | Your OpenWeatherMap API key |
| `ZIP` | `10029` | Your ZIP code (US only) |
| `TELEGRAM_BOT_TOKEN` | `123456:ABC-xyz...` | Bot token from @BotFather |
| `TELEGRAM_CHAT_ID` | `123456789` | Your personal Telegram chat ID |

### 3. 🧪 Test Your Telegram Bot (One-Time Setup)
1. Go to @BotFather in Telegram
2. Create a new bot → copy the token
3. Start a conversation with your bot in Telegram (`/start`)
4. Visit this URL to retrieve your chat ID:

```bash
https://api.telegram.org/bot<your_token>/getUpdates
```

5. Look for:

```json
"chat": { "id": 123456789 }
```

### 4. ⚙️ Customize the Rain Threshold (Optional)
In .weather-check/weather_check.py:

```python
RAIN_THRESHOLD = 0.05  # Inches
```

Adjust this value to your preferred trigger amount.

### 5. 📅 Run on Schedule or Manually
This workflow runs every day at 10 AM UTC. You can also trigger it manually from the Actions tab in GitHub.

```yaml
on:
  schedule:
    - cron: "0 10 * * *"   # Daily at 10 AM UTC
  workflow_dispatch:       # Manual run support
```

🔧 Adjust the cron timing using crontab.guru

---

## 🛠️ Future Improvements
Add weather icons or formatted forecast times

Support multiple locations or daily summaries

Log outputs to a public GitHub Pages dashboard

Integrate with smart irrigation systems

---

## 🙌 Contributing
Pull requests and suggestions are welcome!
Feel free to fork this project, improve the logic, or add more integrations.

---
