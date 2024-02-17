height = float(input("Type your height in meters. \n"))

weight = int(input("Enter your weight in kilogram. \n"))

BMI = round(weight / (height ** height), 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} and You are underweight.")
elif BMI < 24.9:
    print(f"Your BMI is {BMI} and You are perfectly fine")
elif BMI < 29.9:
    print(f"Your BMI is {BMI} and You are overweight. Move up.")
elif BMI < 34.9:
    print(f"Your BMI is {BMI} and Unfortunately you are obese!")
else:
    print(f"Your BMI is {BMI} and YOu are extremely obese!!!!")
