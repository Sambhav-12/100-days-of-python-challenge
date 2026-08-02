# 🐢 Turtle Crossing Capstone Game

A classic **Frogger-style arcade game** built with Python and the `turtle` graphics library. This project serves as Capstone Project #2 in my Python journey, focusing on **Object-Oriented Programming (OOP)**, collision detection, game loop timing, and state management.

---

## 🚀 Features

* **Object-Oriented Architecture:** Modular code split across `Player`, `CarManager`, and `Scoreboard` classes.
* **Dynamic Difficulty:** Cars speed up each time you successfully cross the road and reach the finish line.
* **Randomized Traffic Generation:** Cars are spawned randomly at varying positions with unique colors.
* **Collision Detection:** Precise distance tracking to detect game-over scenarios when colliding with cars.
* **Level & Score Tracking:** Real-time level updates displayed directly on the screen.

---

## 🛠️ Tech Stack & Skills Applied

* **Language:** Python 3
* **Graphics:** Turtle Graphics Module
* **Concepts Used:**
  * Object-Oriented Programming (Classes, Inheritance, Instance Attributes)
  * Event Listeners & Screen Updates (`tracer`, `update`, `onkey`)
  * Lists & Iteration for Dynamic Entity Management
  * Math & Collision Logic

---

## 📂 Project Structure

```text
.
├── main.py          # Central game loop, event handling, collision logic
├── player.py        # Player turtle class, movement controls, reset handling
├── car_manager.py   # Traffic generator, movement physics, level scaling
├── scoreboard.py    # UI text rendering, level tracking, game over screen
└── README.md        # Project documentation
