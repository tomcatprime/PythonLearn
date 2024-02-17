#give the remainder after the division
# 6 % 2 = 0 or 5 % 2 = reminder is 1

#check even or odd 


number  = int(input("Type your number: "))
calculation = number % 2

if calculation == 0:
    print("This is the even number")
else:
    print(f"This is the odd number and the reminder is {calculation}")

