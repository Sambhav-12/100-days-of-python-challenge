# Day 16: OOP Coffee Machine Implementation ☕⚙️

Refactored the procedural Coffee Machine project into an Object-Oriented Architecture using external modules and class abstraction.

## 🚀 Key Architectural Concepts
- **Encapsulation:** Isolated machine functions into distinct classes (`CoffeeMaker`, `MoneyMachine`, `Menu`) to decouple state management from execution.
- **Interface Interaction:** Used method calls (`coffee_maker.is_resource_sufficient()`, `money_machine.make_payment()`) instead of modifying underlying data structures directly.
- **Class Instantiation:** Created concrete instances of domain objects in `main.py` to drive execution flow.

## 💡 Code Highlights
- **State Abstraction:** Interfaced with pre-built methods to handle internal arithmetic, coin collection, and inventory tracking without exposing raw dictionary state.
- **Modular Pipeline:** Connected `Menu.find_drink()` output directly as input parameter objects for `CoffeeMaker` operations.

