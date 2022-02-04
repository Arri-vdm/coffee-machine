"""The Coffee Machine"""

# Import logo
from art import cup, line
from replit import clear

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
    "water": 300,  # Testing 300
    "milk": 200,  # Testing 200
    "coffee": 100,  # Testing 100
}

# Starting balance
balance = 100

# Starting profit amount
profit = 0




def resource_report(current_or_new):
    msg = current_or_new
    print(line)
    print(f"The {msg} resource values:")
    print(line)
    print(f"Water:                                  {resources['water']}ml"
          f"\nMilk:                                   {resources['milk']}ml"
          f"\nCoffee:                                 {resources['coffee']}g")
    print(line)


def refill():
    clear()
    resource_report(current_or_new="CURRENT")
    resource_variables = {"water": "ml", "milk": "ml", "coffee": "g"}
    for key, value in resource_variables.items():
        result = int(
            input(
                f"\nHow much {key.upper()} would you like to add?\nMin. 1{value} to Max. 1000{value}?\nEnter HERE >>> "
            ))
        if 0 <= result <= 1000:
            resources[key] += result
            print(line)
            print(
                f"Thank you.\nAssigning {result}{value} increase to {key.upper()}..."
            )
            print(line)
        else:
            print(line)
            print(
                f"WARNING >>> Outside required limits\nRESULT  >>> {key.upper()} was given a value {result}{value}"
            )
            print(line)
            result = int(
                input(
                    f"\nHow much {key.upper()} would you like to add?\nMin. 1{value} to Max. 1000{value}?\nEnter HERE >>> "
                ))
            if 0 <= result <= 1000:
                resources[key] += result
                print(line)
                print(
                    f"Thank you.\nAssigning {result}{value} increase to {key.upper()}..."
                )
                print(line)
            else:
                print(line)
                print(
                    f"WARNING >>> STILL outside required limits\n"
                    f"RESULT  >>> {key.upper()} was given a value {result}{value}"
                )
                print(line)
                print(
                    f"DEFAULT >>> Assigning 0{value} increase to {key.upper()}..."
                )
                print(line)
    clear()
    resource_report(current_or_new="NEW")
    back_to_menu = input(f"\nEnter 'm' for MENU when ready...\nEnter HERE >>> ")
    if back_to_menu in ("m", "menu"):
        clear()


# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def resources_sufficient(drink_ordered):
    for item in drink_ordered:
        if drink_ordered[item] > resources[item]:
            print(f"\nSorry there is not enough {item}")
            return False
    return True


# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coins():
    print("\nPlease insert coins:")
    total = int(input("How many Quarters  ($0.25):")) * 0.25
    total += int(input("How many Dimes     ($0.10):")) * 0.1
    total += int(input("How many Nickles   ($0.05):")) * 0.05
    total += int(input("How many Pennies   ($0.01):")) * 0.01
    return total


# TODO 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
def Check_transaction(coins_inserted, recipe_cost):
    if coins_inserted >= recipe_cost:
        change = round(recipe_cost - coins_inserted, 2)
        print(f"\nYour change is: {change:.2f}")
        global balance, profit
        balance += recipe_cost
        profit += recipe_cost
        return True
    else:
        print(
            f"\nSorry ${coins_inserted:.2f} is not enough.\nMoney being refunded..."
        )
        return False


# TODO 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
def make_coffee(drink_name, drink_ordered):
    for item in drink_ordered:
        resources[item] -= drink_ordered[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")




# Coffee machine is ON
is_on = True

# While the coffee machine is on
while is_on:

    print(line)
    print("Welcome to your company's COFFEE MACHINE:")
    print(line)
    print(cup)
    print(line)
    # TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.
    user_choice = input("Drink Menu:"
                        "\n-----------------------------------------------"
                        "\nCappuccino - $3.00:                  Enter 'c'"
                        "\nLatte      - $2.50:                  Enter 'l'"
                        "\nEspresso   - $1.50:                  Enter 'e'"
                        "\n-----------------------------------------------"
                        "\nOperations Menu:"
                        "\n-----------------------------------------------"
                        "\nMachine Report    :                  Enter 'm'"
                        "\nRefill            :                  Enter 'r'"
                        "\nSupport           :                  Enter 's'"
                        "\nTurn Off          :                  Enter 'o'"
                        "\n-----------------------------------------------"
                        "\nEnter HERE >>> ").lower()

    # TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
    # the machine. Your code should end execution when this happens.
    if user_choice in ("o", "off"):
        print("\n")
        print(line)
        print(
            "The Coffee Machine is now turning OFF!\nThank you and goodbye...")
        print(line, "\n\n")
        is_on = False

    # TODO 3. Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g
    # Money: $2.5
    elif user_choice in ("m", "machine", "report", "machine report"):
        clear()
        print(line)
        print("The current resource values:")
        print(line)
        print(f"Water:                                  {resources['water']}ml"
              f"\nMilk:                                   {resources['milk']}ml"
              f"\nCoffee:                                 {resources['coffee']}g")
        print(line)
        print(f"Balance:                              ${balance:.2f}"
              f"\nProfit:                               ${profit:.2f}")
        print(line)
        back_to_menu = input(f"\nEnter 'm' for MENU when ready...\nEnter HERE >>> ")
        if back_to_menu in ("m", "menu"):
            clear()
    elif user_choice in ("s", "support"):
        clear()
        print(line)
        print("Support:")
        print(line)
        print(f"Developer:                Armand van der Merwe"
              f"\nEmail:                      arri.vdm@gmail.com")
        print(line)
        back_to_menu = input(f"\nEnter 'm' for MENU when ready...\nEnter HERE >>> ")
        if back_to_menu in ("m", "menu"):
            clear()
    elif user_choice in ("r", "refill"):
        refill()
    else:
        if user_choice in ("c", "cappuccino"):
            user_choice = "cappuccino"
        elif user_choice in ("l", "latte"):
            user_choice = "cappuccino"
        elif user_choice in ("e", "espresso"):
            user_choice = "espresso"
        drink = MENU[user_choice]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if Check_transaction(payment, drink["cost"]):
                make_coffee(drink, drink["ingredients"])
