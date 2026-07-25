from data import MENU
from data import resources

def choice(valid_options):
    user_choice = input("What would you like? (espresso/cappuccino/latte) or (off/report): ").lower()
    while user_choice not in valid_options:
        user_choice = input("Invalid! Please choose a valid option: ").lower()
    return user_choice
def enough_resources(drink):
    for ingredient , amount_needed in drink["ingredients"].items():
        if amount_needed > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True
def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total
def make_coffee(drink, user_choice):
    for ingredient, amount_needed in drink["ingredients"].items():
        resources[ingredient] -= amount_needed
    resources["money"] += drink["cost"]
    print(f"Here is your {user_choice}. Enjoy!")
   
valid_inputs = list(MENU.keys()) + ["off" , "report"]

while True:
    user_input = choice(valid_inputs)
    if user_input == "off":
        break
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        continue
    else:
        coffee = MENU[user_input]
        if not enough_resources(coffee):
            continue
        print(f"That will be ${coffee['cost']}. Please insert coins. ")
        money_inserted = process_coins()
        if money_inserted < coffee["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        else:
            if money_inserted > coffee["cost"]:
                change = round(money_inserted - coffee["cost"], 2)
                print(f"Here is ${change} in change.")
            make_coffee(drink = coffee, user_choice = user_input)

