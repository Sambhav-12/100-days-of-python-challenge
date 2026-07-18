import random
print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_num = int(input("How many nuymbers would you like?\n"))

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Easy 
password1 = ''
for c in range(0, n_letters):
    password1 += random.choice(letters)
for c in range(0, n_symbols):
    password1 += random.choice(symbols)
for c in range(0, n_num):
    password1 += random.choice(numbers)
print(f"your password is {password1}")


# Hard
pl = [] #pl is password list 
for c in range(0, n_letters):
    pl.append(random.choice(letters))
for c in range(0, n_symbols):
    pl.append(random.choice(symbols))
for c in range(0, n_num):
    pl.append(random.choice(numbers))
random.shuffle(pl) #shuffle keyword shuffles the list order randomly
password2 = ''
for c in pl:
    password2 += c

print(f"your password is {password2}")