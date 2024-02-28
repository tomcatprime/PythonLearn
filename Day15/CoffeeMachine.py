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

#report of resources
def report():
    for item in resources:
        level = resources[item]
        resource = item.title()
        print(f"{resource}: {level}ml")


# TODO: 1. Write Program
isFinish = False

while not isFinish:
    userChoice = input("What would you like? (espresso/latte/capuccino)").lower()
    # access variables
    if userChoice == "espresso":
        #ingredients
        water = MENU[userChoice]["ingredients"]["water"]
        newWater = resources["water"] - water
        resources["water"] = newWater
        water = MENU[userChoice]["ingredients"]["coffee"]
        print(water)
        cost = MENU[userChoice]["cost"] #price
        print(cost)
    elif userChoice == "latte":
        #water
        water = MENU[userChoice]["ingredients"]["water"]
        newWater = resources["water"] - water
        resources["water"] = newWater

        #milk
        milk = MENU[userChoice]["ingredients"]["milk"]
        newMilk = resources["milk"] - milk
        resources["milk"] = newMilk
        print(resources)

    elif userChoice == "report":
        report()

