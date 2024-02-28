# program requirments
# 1. Print report
# 2. Check resources sufficient
# 3. Process coins
# 4. Check transaction successfull
# 5. Make Coffee


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

def isResourceSufficient(order_ingredient):
    """Returns True when order can be made, False if ingredients are insufficients """
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


profit = 0

def report():
    print(f"Profit: ${profit}")
    for item in resources:
        level = resources[item]
        resource = item.title()
        print(f"{resource}: {level}ml")


def processCoins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def isTransactionSuccessful(moneyReceived, drinkCost):
    """Return true when the payment is accepted, or False if money is insufficient"""
    if moneyReceived > drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change}")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enought. Money refunded.")
        return False

def makeCoffee(drinkName, orderIngredients):
    """Deduct the required ingredients from the resources. """
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName} ☕")

isRunning = True
while isRunning:
    choice = input("What would you like? (espresso/latte/cappuccino)").lower()
    if choice == "off":
        isRunning = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink["ingredients"]):
            payment = processCoins()
            if isTransactionSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])






