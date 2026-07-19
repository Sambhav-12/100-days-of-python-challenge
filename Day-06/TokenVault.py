def validate_token(token):
    if token == "OPEN_SESAME":
        return True
    else:
        return False

def calculate_attempts_left(max_attempts, current_attempts):
    return max_attempts - current_attempts

MAX_ATTEMPTS = 3
attempts_used = 0
is_vault_locked = True

while is_vault_locked and attempts_used < MAX_ATTEMPTS:
    key = input("Enter Token: ")
    attempts_used += 1
    attempts_left = calculate_attempts_left(MAX_ATTEMPTS, attempts_used)
    if validate_token(key):
        print("Open!")
        is_vault_locked = False
    else:
        print("Blah! Try again!")

    if attempts_left == 0:
        print("Out of attempts!")
    else:
        print(f"Attempts used: {attempts_used}\nAttempts left: {attempts_left}")
    


