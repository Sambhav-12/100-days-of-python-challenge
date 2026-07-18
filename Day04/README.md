# Day 4: Randomization and Python Lists

## What I Built
* **Heads or Tails:** A simple binary probability generator using the random module.
* **Banker Roulette:** A program that randomly selects a friend from a list to pay the bill, utilizing both index selection and `random.choice()`.The `random.choice()` method is what I get to know from the course , the index selection is what I made.
* **Rock Paper Scissors (Method 1 & 2):** Built using independent conditional logical combinations (`and`), tracking choices cleanly using list indexing instead of relying on complex mathematical comparison inequalities.

## Key Concepts Learned
* **The Random Module:** Explored random integer generation (`randint`) and automated list selection (`choice`).
* **Python Lists:** Learned about sequential data storage, mutability, and expanding structures using methods like `.append()`.
* **Zero-Based Indexing:** Solidified the rule that lists begin counting at index `0`, making the final element index `len(list) - 1`.` and `.extend()

## Errors Faced & Solved
* **IndexError Mitigation:** Identified how out-of-bounds inputs crash list references. Noted the importance of filtering out input numbers greater than the valid indices before processing logic paths.

## Experience
Originally , the RPS program has ASCII art but i dont like to use them because they made code looks a bit dull and takes a lot space so i avoid using them. I used them previously in my `Day - 03 , treasure island code ` though.
Today , learned many new things and also the first time where the dissimilarities between my code and teachers code is too much, she used mathematics way using comparison operators whereas , i used logical operators though we need to write almost same number of line of code still.
