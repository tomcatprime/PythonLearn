# 1st input: enter height in meters e.g: 1.65
height = input("Type your height: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Type your weight: ")
# 🚨 Don't change the code above 👆
newHeight = float(height)
newWeight = int(weight)

# Write your code below this line 👇
bmi = newWeight / (newHeight ** 2) #exponent operator ** number - will square number
print(int(bmi))

#rounding numbers
print(round(8 / 3, 2))

#floor division
print(8 // 3) #floor division


score = 0
score += 1
print(score)
score -= 2
print(score)

isWinning = True
#f-string combining types  f"text text text {}"

print(f"{score} is combined with {isWinning} and also combined with {newHeight}")


