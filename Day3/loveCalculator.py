print("The Love Calculator is calculating your score...")
name1 = input("type your name: \n") # What is your name?
name2 = input("type your partner name: \n") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combinedNames = name1 + name2
loverNames = combinedNames.lower()

t = loverNames.count("t")
r = loverNames.count("r")
u = loverNames.count("u")
e = loverNames.count("e")
true = t + r + u + e

l = loverNames.count("l")
o = loverNames.count("o")
v = loverNames.count("v")
e = loverNames.count("e")
love = l + o + v + e


score = int(str(true) + str(love))


if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
