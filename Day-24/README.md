# Day 24: File I/O, Paths & Automated Mail Merge 📁✍️

## 📌 Overview
Mastered Python file system operations, context managers (`with` statements), string manipulation utilities (`strip()`, `replace()`), and relative vs. absolute paths by building an automated letter generation script.

---

## 🛠️ Key Concepts & Implementation
* **Context Managers (`with open(...)`):** Safely handled file reading and writing streams, ensuring automatic resource cleanup and stream closure upon block exit.
* **Path Resolution:** Managed directory structures using relative and absolute file paths to locate templates and target outputs reliably.
* **String Parsing & Transformation:** Used `.readlines()` to ingest raw text data, `.strip()` to clean formatting whitespace, and `.replace()` to dynamically swap placeholder text with target recipient names.
* **Automated Batch Generation:** Programmatically iterated over a dataset of names to generate unique, personalized correspondence files saved to designated directories.

---

## 📂 Project Architecture
* **`main.py`** — Core execution script managing file input streams, string replacement loops, and file output creation.
* **Input/Output Text Assets** — Plain text databases for raw names, template strings, and generated result files.
