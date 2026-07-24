# Day 14: Higher Lower Game (CLI Capstone) 📈

A Command Line Interface implementation of the classic Higher Lower game, serving as the capstone project for Python beginner fundamentals. The game compares real-world data metrics (follower counts) across popular accounts.

## 🚀 Features
- **Distinct Selection Engine:** Utilizes Python's `random.sample()` to pull guaranteed distinct comparisons on initialization.
- **Winner Continuation:** Automatically shifts the winning account to position `A` for the next round while generating a non-overlapping challenger for position `B`.
- **Defensive Input Validation:** Traps invalid inputs (`while user_choice not in ("a", "b")`) before evaluating game state.

## 💡 Key Engineering Takeaways
- **Modular Function Isolation:** Separated data fetching (`second_account()`) and input processing (`choice()`) from the primary control loop to reduce logical complexity.
- **Ternary State Management:** Simplified conditional evaluation using concise, readable Python statements.
- **Refactoring:** Cleaned up redundant loop structures by leveraging Python's built-in standard library utilities.
