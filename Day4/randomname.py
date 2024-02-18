import random
names_string = input("Type names: ")
names = names_string.split(", ")
countLenght = len(names)

randomNum = random.randint(0,countLenght - 1)
whoWillPay = names[randomNum]

print(f"{whoWillPay} is going to buy the meal today!")