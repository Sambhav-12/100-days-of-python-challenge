# Day 34: Dynamic OOP Quiz Engine (API Integration & Type Hinting) 🧠⚡

## 📌 Overview
Upgraded the console-based quiz application (Day 17) into a dynamic, event-driven GUI application. Integrated real-time data fetching from the Open Trivia Database API, implemented HTML entity unescaping, and enforced object-oriented class separation between business logic and UI state.

---

## 🛠️ Key Technical Implementations
* **API Data Ingestion:** Fetched boolean trivia questions dynamically using `requests.get()` with custom query parameters (`amount`, `type`).
* **HTML Decoding:** Used Python's `html.unescape()` module inside `QuizBrain` to sanitize raw HTML entities (e.g., `&quot;`, `&#039;`) into clean string payloads.
* **Type Hinting:** Implemented explicit class type hints (`quiz_brain: QuizBrain`) in constructor interfaces to ensure robust static type checking and auto-completion.
* **Asynchronous UI Feedback:** Created dynamic user feedback loops using Tkinter's `.config(bg=...)` combined with `window.after(1000)` to execute delayed canvas refreshes after answer evaluation.

---

## 📂 Architecture
* **`main.py`** — Application entry point initializing object instances and passing execution control to the UI mainloop.
* **`data.py`** — API fetch module retrieving dynamic trivia questions.
* **`quiz_brain.py`** — Core business logic managing question sequence tracking, HTML decoding, and scoring logic.
* **`ui.py`** — `QuizeInterface` class managing canvas states, user input events, and visual color feedback.
* **`question_model.py`** — Data model standardizing question object schemas.
