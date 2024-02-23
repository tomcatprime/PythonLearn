# HINT: You can call clear() to clear the output in the console.
print("Welcome in blind auction program")
import os

print("Let's start")
isGameEnd = False

biders = {}


def auctionList(name, bid):
    auction = {}
    name = biders[name]
    print(name)


while not isGameEnd:
    name = input("What is your name?\n")
    bid = int(input("What is your bid? \n"))
    auctionList(name, bid)
    other_user = input("Are there other users who want to bid?: \n")
    if other_user == "no":
        isGameEnd = True
        score = 0
        print(biders)

        # for name in biders:
        #     if biders[name] >= score:
        #         score = biders[name]
        #     print(score)

    else:
        os.system("clear")
print(biders)
