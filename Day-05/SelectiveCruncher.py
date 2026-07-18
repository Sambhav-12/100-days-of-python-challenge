# Its a custom challenge for me from AI
for n in range(1,51):
    # If a number is divisible by 2, print its square
    # If a number is divisible by 7, skip it entirely(use continue keyword)
    # If a number is a multiple of both 3 and 8, print max limit reached and stop(use break keyword)

    if n % 3 == 0 and n % 8 == 0:
        print("Max limit reached")
        break
    elif n % 7 == 0:
        continue
    elif n % 2 == 0:
        print(n**2) 
    else:
        print(n)
    