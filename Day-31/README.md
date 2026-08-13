# Day 31: Flash Card GUI Capstone Project 🎴🇫🇷

## 📌 Overview
Built an interactive Flash Card Language Learning desktop application with Tkinter and Pandas. Features asynchronous card-flipping timers, visual UI state changes, and persistent progress tracking using localized CSV storage.

---

## 🛠️ Key Architectural Elements
* **State & Timer Control:** Managed delayed visual feedback (card flipping from front language to back translation) using `window.after()` callbacks and `after_cancel()` resets.
* **Resilient Data Streams:** Implemented `try...except FileNotFoundError` error handling to seamlessly transition between default word sets and user-specific saved progress (`words_to_learn.csv`).
* **Dynamic Record Mutation:** Converted Pandas DataFrames to dictionary record lists (`orient="records"`), removing mastered cards dynamically and updating memory logs via `to_csv(index=False)`.
* **Tkinter Canvas Component Manipulation:** Swapped layered canvas background graphics (`create_image`) and text properties (`itemconfig`) on user trigger events.

---

## 📂 Project Architecture
* **`main.py`** — Primary application logic, timer state management, Pandas CSV operations, and Tkinter GUI layout.
* **`data/`** — Folder containing initial vocabulary CSV datasets and updated progress logs.
* **`images/`** — Visual UI canvas assets (card front, card back, checkmark, cross buttons).
