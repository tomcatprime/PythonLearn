# HINT: You can call clear() to clear the output in the console.
print("Welcome in blind auction program")
import os

print("Let's start")


bids = {}
isGameEnd = False


def findHighestBidder(bidding_records):
    highestBid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highestBid:
            highestBid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")


while not isGameEnd:
    name = input("What is your name?\n")
    price = int(input("What is your bid?: $ \n"))
    bids[name] = price
    should_continue = input("Are there any others bidders? Type 'yes' or 'no.\n")
    if should_continue == "no":
        isGameEnd = True
        findHighestBidder(bids)
    else:
        os.system("clear")
