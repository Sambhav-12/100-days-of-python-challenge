from gamedata import data
import random

# A function to check if the challenger has same value as the winner to fix the overlapping of them and not making another block of code in loop
def second_account(winner):
    challenger = random.choice(data)
    while challenger == winner:
        challenger = random.choice(data)
    return challenger

def choice():
    user_choice = input("Who has more followers? Type 'a' or 'b': ").lower()
    # if a user type a string or numbers, while loop will start to take only A or B as input.
    while user_choice not in ("a" , "b"):
        user_choice = input("Invalid! Type 'a' or 'b': ").lower()
    return user_choice

# sample will take data from data list and it will be distinct and no repetition which will help us to not make an unnecessary while loop for that
account_a , account_b = random.sample(data, 2)

score = 0
game_over = False
while not game_over:
    print(f"Compare A:\n{account_a['name']}, {account_a['description']}, {account_a['country']}")
    print(f"Against B:\n{account_b['name']}, {account_b['description']}, {account_b['country']}")
    user_input = choice()
    if user_input == "a":
        comparison = account_a['followers'] > account_b['followers']
    else:
        comparison = account_b['followers'] > account_a['followers']

    if comparison:
        winner = account_a if user_input == "a" else account_b
        challenger = second_account(winner)
        account_a, account_b = winner, challenger
        score += 1
        print(f"Correct! Your score is: {score}")
    else:
        game_over = True
        print(f"Sorry, You Lost!\nFinal Score: {score}")