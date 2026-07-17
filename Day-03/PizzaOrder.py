print("Welcome to Pizza Delieveris!")
size = input("What size pizza do you want?S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
"""
S - $15
M- $20
L - $25
pepperoni for small - $2
pepperoni for medium or large - $3
extra cheese - $1 
"""

#todo: work out how much they need to pay their size choice
bill = 0
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("please choose the given size")

#todo: work out how much to add their bill based on their pepperoni choice.
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

#todo: work out their final amount based on whether if they need extra cheese.
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is {bill}")
