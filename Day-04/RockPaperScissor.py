# Rock -> scissor
# paper -> rock
# scissor -> paper
import random
print("---------METHOD - 1-----------")


n=int(input("Type 0 for rock , 1 for paper and 2 for scissors: "))
cn = random.randint(0,2)
if n < 0 and n > 2:
    print("Invalid Choice!")
if n == 0 and cn == 2:
    print("You won!")
elif n == 1 and cn == 0:
    print("You won!")
elif n == 2 and cn == 1:
    print("You won!")
elif n == 0 and cn == 1:
    print("You lose!")
elif n == 1 and cn == 2:
    print("You lose!")
elif n == 2 and cn == 0:
    print("You lose!")
elif n == cn:
    print("Ties")
else: 
    print("Please type the right number")


print("---------METHOD - 2-----------")


rps = ['rock' , 'paper' , 'scissors']
n1 = int(input("Type 0 for rock , 1 for paper and 2 for scissors: "))
cn1 = random.randint(0,2)
if n1 < 0 and n1 > 2:
    print("Invalid Choice!")
if n1 == 0 and cn1 == 2:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("You won!")
elif n1 == 1 and cn1 == 0:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("You won!")
elif n1 == 2 and cn1 == 1:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("You won!")
elif n1 == 0 and cn1 == 1:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("You lose!")
elif n1 == 1 and cn1 == 2:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("You lose!")
elif n1 == 2 and cn1 == 0:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("You lose!")
elif n1 == cn1:
    print(f"your choice {rps[n1]} and computers choice {rps[cn1]}")
    print("Ties")
else: 
    print("Please type the right number")
