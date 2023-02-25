MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def print_report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : {money}")


def check_resources(ingredients):
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False

    return True


def process_coins():
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def transaction(inserted_amount, drink_cost):
    if inserted_amount < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is your ${inserted_amount - drink_cost} in change.")
        global money
        money += drink_cost
        return True


def make_coffee(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink} ☕️. Enjoy!")


def coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    enough_resources = False
    user_coins = 0
    success = False

    if user_choice == 'off':
        print("Goodbye!")
        exit()
    elif user_choice == 'report':
        print_report()
        coffee_machine()
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        enough_resources = check_resources(ingredients=MENU[user_choice].get("ingredients"))

        if enough_resources:
            user_coins = process_coins()
            success = transaction(user_coins, drink_cost=MENU[user_choice].get("cost"))

            if success:
                make_coffee(user_choice, order_ingredients=MENU[user_choice].get("ingredients"))
                coffee_machine()
            else:
                coffee_machine()
        else:
            coffee_machine()
    else:
        print("Invalid input. Please try again")
        coffee_machine()


coffee_machine()
