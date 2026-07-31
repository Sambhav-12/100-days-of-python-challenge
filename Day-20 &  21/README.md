# Day 20 & 21: Modular OOP Snake Game 🐍

## 📌 Overview
Built a full-featured classic Snake Game utilizing multi-file Object-Oriented Architecture, Class Inheritance, event listener mechanics, and collision physics.

---

## 🛠️ Architecture & Concepts
* **Class Inheritance:** Built `Food` and `Scoreboard` classes that inherit directly from `turtle.Turtle`, leveraging `super().__init__()` to extend existing GUI components with custom methods.
* **Encapsulated State Management:** Created a self-contained `Snake` module to control array segment movement using reverse index loops (`range(len-1, 0, -1)`).
* **Collision Math & Physics:** Implemented distance checks (`snake.head.distance()`) for food pickup and tail collisions, alongside bounding box limits ($\pm280$) for wall boundaries.
* **Screen Refresh Management:** Used `screen.tracer(0)` and manual `screen.update()` loops to prevent UI flickering during frame redraws.

---

## 📂 Project Structure
* **`snakegame.py`** — Main execution loop, event listener registration, and game state validation.
* **`snake.py`** — `Snake` class handling movement, segment appending, and directional controls.
* **`food.py`** — `Food` class handling randomized coordinate positioning.
* **`scoreboard.py`** — `Scoreboard` class handling score updates and Game Over canvas rendering.

---

## 🚀 Key Takeaways
Dividing application logic into modular files based on single-responsibility principles dramatically improves code readability and simplifies debugging across complex interactive software.
