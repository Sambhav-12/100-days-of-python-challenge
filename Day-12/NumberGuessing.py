import random

computer_num = random.randint(1,100)
HARD_LEVEL = 5
EASY_LEVEL = 10
level_attempts = {
    "easy" : EASY_LEVEL,
    "hard" : HARD_LEVEL,
}
user_choice = input("Choose difficulty! Type 'easy' or 'hard': ").lower()
while user_choice not in level_attempts:
    user_choice = input("Invalid! Type 'easy' or 'hard': ").lower()
attempts = level_attempts[user_choice]
print(f"You have {attempts} attempts.")

game_over = False
while not game_over:
    guess = int(input("Enter the num: "))
    if guess == computer_num:
        print(f"You won! The number is {computer_num}")
        game_over = True
    else:
        attempts -= 1
        if attempts == 0:
            print(f"You ran out of attempts")
            print(f"The correct number is {computer_num}")
            game_over = True
        else:
            print(f"You have {attempts} attempts. Try again!")
            if guess > computer_num:
                print("Too High!")
            else:
                print("Too Low!")
        
    


