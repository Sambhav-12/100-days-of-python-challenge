# Day 27: Tkinter GUI & Flexible Arguments (*args / **kwargs) 🖥️📐

## 📌 Overview
Explored Python's dynamic argument handling (`*args` for tuple packing, `**kwargs` for dictionary unpacking) and built desktop applications using `tkinter`. Developed a Miles-to-Kilometers Converter utilizing `grid()` matrix layouts and event-driven function bindings.

---

## 🛠️ Key Concepts & Implementation
* **Dynamic Arguments (`*args`, `**kwargs`):** Mastered variadic function signatures, understanding parameter packing into tuples and dictionaries for scalable API definitions.
* **Tkinter Layout Architecture:** Compared `pack()`, `place()`, and `grid()` layout managers, utilizing `grid()` matrix positioning (`column`, `row`) for scalable UI component alignment.
* **Event-Driven Binding:** Tied UI buttons (`Button(command=...)`) to dynamic callback functions to extract user input (`Entry.get()`), execute arithmetic conversions, and update label properties (`Label.config()`).
* **Padding & Window Styling:** Applied UI window configuration (`window.config(padx=20, pady=20)`) for visual spacing.

---

## 📂 Architecture
* **`main.py`** — Experimental Tkinter script testing label updates, button interactions, and layout managers.
* **`converter.py`** — Functional Miles-to-Km conversion app built using structured grid layouts.
