# Day 28: Graphical Pomodoro Timer & Event Loops ⏱️🍅

## 📌 Overview
Built a fully functional Pomodoro GUI application utilizing `tkinter.Canvas` for element layering, dynamic image rendering, and recursive asynchronous timing loops using `window.after()`.
To be honest, most of the code is done by teach though I myself tried to do somethings but couldn't do that much.
---

## 🛠️ Key Concepts & Implementation
* **Canvas Layering:** Rendered complex graphic components using `Canvas.create_image()` and `Canvas.create_text()` to place dynamic countdown overlays directly onto visual assets.
* **Asynchronous Timing Engine:** Managed recursive timer intervals without blocking the primary GUI main thread using `window.after()` callbacks.
* **Timer Cancellation & Reset:** Captured event loop signatures to safely clear scheduled callbacks using `window.after_cancel()`.
* **Dynamic State Logic:** Built automated state switching (Work vs. Short/Long Breaks) driven by execution cycle counters (`reps`) and conditional modulo arithmetic.

---

## 📂 Architecture
* **`main.py`** — Complete execution loop, timer callback engine, canvas rendering, and state management.
* **`tomato.png`** — Background asset for visual GUI composition.
