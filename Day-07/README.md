# Day 7: Hangman CLI Game & Input Hardening

## What I Built
A robust, multi-file command-line implementation of the classic Hangman game. The application manages visual ASCII stages, tracks remaining lives, and enforces defensive input validation to prevent invalid entries or duplicate guesses from corrupting game state.

## Key Concepts Learned
- **Control Flow & Guard Clauses:** Using `continue` to short-circuit loop iterations on invalid or duplicate inputs before primary game logic executes.
- **Defensive Programming:** Hardening the application against unexpected user inputs using length checks (`len()`) and string methods (`isalpha()`).
- **State Management:** Tracking player state (`lives`, `guessed_letters`) across a continuous `while` execution loop.
- **Modular File Architecture:** Separating game assets and dictionary word banks into standalone files (`hangman_words.py`, `hangman_arts.py`) imported into the core executable.

## Errors Faced & Solved
- **Bug 1 (Duplicate Deductions):** Re-guessing previously entered letters resulted in multiple life deductions.
  - *Solution:* Used a `continue()`  keyword to solve that life deduction thing.

## Experience
Today, I got stuck a lot. First, in the code but because the teach uses todo's it becomes easy to go forward still I blunder at some points and had to follow along. I thought i can make this code by myself, but i was completely wrong. Other than this I faced an error in the repeated word and deduction thing i talked above and it was not that hard though but yeah i blundered there too and one more thing to tell you guys is that `continue()` skips loop not if block. I was thinking that it skips if block and was not using it until i remmebered that we can use `continue(0` and `break()` inside a loop for a reason. Honestly, good learning today
