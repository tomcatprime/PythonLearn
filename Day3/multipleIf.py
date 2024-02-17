#nested if  -   elif

print("Welcome to the rollercoaster!")
height = int(input("What is your geight in cm?"))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
        
    elif age < 18:
        bill = 7
        print("Please pay $7.")

    else:
        bill = 12
        print("Please pay $12.")
    wantsPhoto = input("Do you want a photo taken? Y or N.")
    if wantsPhoto == "Y":
        #add $3 to the bill
        bill += 3
    print(f"YOur final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

