# Day 26: List & Dictionary Comprehensions + NATO Phonetic Converter 🔤

## 📌 Overview
Mastered Python List, Dictionary, and DataFrame comprehensions. Replaced traditional verbose loops with single-line declarative expressions to process file stream intersections and build a NATO Phonetic Alphabet converter.

---

## 🛠️ Key Implementation & Concepts
* **Data Overlap via List Comprehensions:** Filtered common integers across two distinct text files (`file1.txt`, `file2.txt`) using conditional list comprehensions (`[num for num in numbers1 if num in numbers2]`).
* **DataFrame Iteration (`.iterrows()`):** Transformed dynamic CSV tabular data into high-speed lookup dictionaries using Pandas row iteration (`{row.letter: row.code for (index, row) in data.iterrows()}`).
* **Input Sanitization & Processing:** Sanitized raw string inputs using `.replace(" ", "").upper()` to map characters dynamically to phonetic alphabet values.

---

## 📂 Architecture
* **`task.py`** — File parsing script finding numerical set intersections between two datasets.
* **`main.py`** — Interactive command-line tool converting strings into NATO phonetic equivalents using Pandas lookup dictionaries.
* **`nato_phonetic_alphabet.csv`** — Target dataset mapping uppercase characters to NATO code words.
