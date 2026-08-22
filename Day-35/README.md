# Day 35: Weather Alert & SMS Notifier (API Authentication & Environment Variables) 🌧️📱

## 📌 Overview
Built an automated weather monitoring script that queries weather forecast APIs to check if rain or severe weather is predicted in a target location over the next 12 hours. If rain is detected, it triggers an automated notification using Twilio/Telegram APIs. The project enforces production security standards by abstracting sensitive API keys and tokens into system environment variables.

---

## 🛠️ Key Technical Implementations
* **API Authentication & Parameters:** Integrated OpenWeatherMap's forecast endpoint using standard HTTP query parameters (`lat`, `lon`, `appid`) via Python's `requests` library.
* **Payload Slicing & Parsing:** Extracted dynamic hourly forecast data using list slicing (`weather_data[:12]`) and evaluated conditional weather condition codes (IDs < 600 indicate rain/snow).
* **System Environment Variables:** Abstracted sensitive credentials out of the codebase using `os.environ.get()` and local `.env` files to prevent accidental security credential leaks on remote repositories.
* **Automated Cloud Dispatch:** Configured environment variable exports on cloud runners (PythonAnywhere / GitHub Actions / Render) for headless daily execution without hardcoded values.

