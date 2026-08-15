# Day 33: Kanye Quotes Generator (API Integration) 🗣️💡

## 📌 Overview
Built an interactive quote generator app using Python's `requests` library to fetch live data from a RESTful API and display dynamic text within a custom Tkinter graphical user interface.

---

## 🛠️ Key Technical Implementations
* **REST API Ingestion:** Established HTTP `GET` requests to the `kanye.rest` endpoint using the `requests` module.
* **Error Handling:** Utilized `response.raise_for_status()` to catch and surface HTTP error codes (e.g., 404, 500) before processing data.
* **JSON Serialization:** Converted raw HTTP response objects into Python dictionaries via `.json()` to extract targeted key-value pairs.
* **Dynamic GUI Updates:** Bound the API execution engine to a Tkinter `Button` event, updating the `Canvas` text element in real-time with `canvas.itemconfig()`.

---

## 📂 Architecture
* **`main.py`** — Primary application script containing the API request handler and Tkinter interface logic.
* **`background.png`** — Canvas speech bubble graphic asset.
* **`kanye.png`** — Custom image button asset triggering quote fetches.
