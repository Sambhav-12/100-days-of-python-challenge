# Day 2: Tip Calculator

## What I Built
A tip calculator that takes a total bill, calculates the tip percentage (10%, 12%, or 15%), asks for the number of people splitting the bill, and outputs the exact amount each person owes using f-strings.

## Key Concepts Learned
* **Data Types & Typecasting:** Learned converting data using `int()`, `float()`, and `str()`. Learned that `input()` always returns a string.
* **Mathematical Operations:** Practiced using PEMDAS, exponents (`**`), and floor division (`//`).
* **Number Manipulation:** Used the `round()` function to format decimals.
* **F-Strings:** Learned how to cleanly embed variables into print statements without painful string concatenation.
* **Data Type Limitations:** Discovered that `len()` throws a `TypeError` if used on integers or booleans; it only works on collection types (strings, lists, tuples, etc.).

## Errors Faced & Solved
* **Math Logic Error:** Initially tried adding percentages instead of multiplying. Solved by breaking down the formula into calculating the tip value first, then adding it back to the base bill.
* **ValueError:** Get to know, this when trying to pass an empty or text string into a `float()` function. Learned that data must look like a number to be cast into a number.

## Experience
In Day 2 , i learned quite a good numebr of things as a beginner like the typecasting and implicit conversion of python. The one and only thing that i get to know on day 2 that i dont know before is that the major difference between / and // , you see the / converts the divisino into float pretty much known by everyone 
but // converts it in integer and we should only use it when we know that the answer is in integer not everywhere as it will make calculations wrong 
