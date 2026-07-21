# Day 8: Caesar Cipher & Function Mechanics

A Python implementation of the classic **Caesar Cipher** encryption and decryption tool, built as part of the *100 Days of Code* curriculum. This project focuses on writing modular, reusable code, managing positional vs. keyword arguments, and applying defensive programming patterns for state management.

---

## 📌 Features

- **Bidirectional Cipher Engine:** Encrypts (encodes) and decrypts (decodes) text messages using dynamic shift values.
- **Defensive Character Preservation:** Non-alphabetic characters (spaces, numbers, special symbols) remain intact and unshifted.
- **Mathematical Bound Handling:** Uses modulo arithmetic (`%`) to handle shift amounts greater than 26 without index out-of-range errors.
- **State-Driven Execution Loop:** Interactive CLI that stays active for multiple operations until explicitly terminated by the user.

---

## 🛠️ Key Concepts Mastered

### 1. Functions with Inputs & Parameter Scoping
Understanding the distinction between **parameters** (variables defined in the function signature) and **arguments** (actual values passed during function calls).

### 2. Positional vs. Keyword Arguments
Implementing explicit keyword arguments (`original_text=text`, `shift_amount=shift`, `encode_or_decode=direction`) to improve readability and prevent silent execution bugs.

### 3. Modular Sign Inversion
Replacing redundant `if/else` execution blocks with mathematical operations (`shift_amount *= -1`) to cleanly handle direction flips for encoding vs. decoding.

### 4. State Flag Control
Managing program lifecycle using Boolean state flags (`should_continue = True`) paired with user input validation inside `while` loops.

---

## 🚀 How It Works

1. **Input Collection:** Prompt the user for:
   - Operation mode (`encode` or `decode`).
   - Plaintext message.
   - Numerical shift value.
2. **Output Generation:** Rebuilds string iteratively and prints the transformed result.
3. **Re-execution Prompt:** Offers a clean exit route or restarts the loop.

---

## 🖥️ Usage Example

```text
  ____                                   ____ _     _               
 / ___|__ _  ___  ___  __ _ _ __        / ___(_)_ _| |__   ___ _ __ 
| |   / _` |/ _ \/ __|/ _` | '__|      | |   | | '_ \ '_ \ / _ \ '__|
| |__| (_| |  __/\__ \ (_| | |    _    | |___| | |_) | | | |  __/ |   
 \____\__,_|\___||___/\__,_|_|   ( )    \____|_| .__/|_| |_|\___|_|   
                                 |/            |_|                    

Type 'encode' to encrypt, and 'decode' to decrypt:
> encode
Type your message:
> hello world 2026
Type the shift number:
> 5

Here is the encoded result: mjqqt btwqi 2026

Type 'yes' to restart and 'no' to exit:
> no
Goodbye!
