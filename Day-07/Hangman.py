import random
from hangman_words import word_list
from hangman_arts import stages

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += ' _ '
print(placeholder)

over = False
correct_letters = []

while not over:
    print(f"----------------{lives}/6 LIVES LEFT-----------------")
    guess = input("Enter the letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        print(stages[lives])
        continue
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter exactly one single letter.")
        print(stages[lives])
        continue

    display = ' '

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += ' _ '
    print(f" {display} ")



    if guess not in chosen_word:
        lives -= 1
        print("You lost a life!")
        if lives == 0:
            over = True
            print(f"-------------------------It was {chosen_word}. You Lose!--------------------------")

    if " _ " not in display:
        over = True
        print(f"-----------------You win! The word is {chosen_word}-----------------") 
    
    print(stages[lives])