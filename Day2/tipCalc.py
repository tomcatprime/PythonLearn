print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 , or 15? "))
split = int(input("how many people to split the bill? "))

tipCalc = bill * (tip / 100)
billPlusTip = bill + tipCalc

splitBill = billPlusTip / split
finalAmount = "{:.2f}".format(splitBill) #round to 2 decimal 
print(f"Each person should pay: ${finalAmount}")

