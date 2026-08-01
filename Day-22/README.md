# Day 22: OOP Classic Pong Arcade 🏓

## 📌 Overview
Built a 2-player Pong arcade game utilizing multi-instance OOP, coordinate mechanics, vector inversion physics, and speed scaling loops.

---

## 🛠️ Architecture & Concepts
* **Vector Inversion Physics:** Handled ball collisions and bounce mechanics by multiplying directional increments (`x_move`, `y_move`) by `-1`.
* **Dynamic Speed Scaling:** Reduced sleep latency continuously on paddle impacts (`move_speed *= 0.9`) to simulate increasing game velocity.
* **Multi-Instance Reuse:** Instantiated a single `Paddle` class twice with separate screen placement vectors `(350, 0)` and `(-350, 0)` and independent key mappings.
* **Dynamic Canvas Score Tracking:** Encapsulated score variables inside a `Scoreboard` class using `turtle.write()` and canvas refreshes (`self.clear()`) on point updates.
