# Day 25: US States Game & Intro to Pandas 🗺️📊

## 📌 Overview
Explored data analysis in Python using `pandas` to process tabular data (`50_states.csv`), combined with `turtle` for dynamic GUI text placement on a map canvas.

---

## 🛠️ Key Implementation & Concepts
* **Pandas Data Alignment:** Read state coordinate data using `pandas.read_csv()`, extracting vectorized coordinates via conditional filtering (`data[data.state == answer_state]`).
* **Path Resolution & Debugging:** Resolved dynamic working directory path errors for embedded asset loading (`.gif` images and `.csv` files).
* **Data Processing & Export:** Implemented list comprehensions/loops to identify missed states on `Exit` and exported the remaining dataset into a structured `states_to_learn.csv` for analysis.
* **Dynamic GUI Rendering:** Placed dynamic labels at precise X/Y pixel coordinates on a visual map layout based on user input matches.

