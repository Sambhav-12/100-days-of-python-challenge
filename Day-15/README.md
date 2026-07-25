# Day 15: Coffee Machine System (CLI Capstone) ☕

A state-driven Command Line Interface (CLI) application simulating a commercial coffee vending machine, payment processing, and input validation.

## 🚀 Features
- **Dynamic Resource Checking:** Iterates through ingredient key-value pairs dynamically to check availability without assuming fixed recipes.
- **Transactional State Management:** Deducts global inventory levels and increments revenue tracking only upon successful payment verification.
- **Defensive Payment Logic:** Calculates coin totals ($0.25, $0.10, $0.05, $0.01), handles exact change calculations using floating-point rounding, and issues immediate refunds on underpayment.

## 💡 Engineering Takeaways
- **Loop Control Precision:** Used `continue` statements to bypass remaining execution steps and reset the main event loop cleanly on state failures (e.g., missing resources or insufficient funds).
- **Separation of Concerns:** Isolated input sanitization, dynamic payment handling, and state mutation into modular helper functions.
