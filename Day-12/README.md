### 📄 README: Day 12 — Number Guessing Game
A DIY number-guessing game designed around defensive programming, input validation, and dictionary-based state lookups.

## 🚀 Features
- **Difficulty Modes:** Configurable difficulty settings ("Easy" with 10 attempts vs. "Hard" with 5 attempts).
- **Input Validation:** Built-in `while` loop that traps invalid user inputs before starting game logic.
- **Feedback Engine:** Gives instant "Too High" / "Too Low" hints while tracking remaining attempt counts.

## 💡 Key Engineering Takeaways
- **Data-Driven Configuration:** Replaced redundant `if/elif` chains with a clean dictionary lookup (`level_attempts[user_choice]`) to map difficulty levels to attempts.
- **Defensive Programming:** Handled string sanitization (`.lower()`) and guarded input prompts to ensure zero runtime crashes on unexpected user input.
- **Linear Design:** Focused on explicit, un-overengineered control flow to keep logic state tracking simple and readable
