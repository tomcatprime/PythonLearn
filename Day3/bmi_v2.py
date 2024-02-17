height = float(input("Type your height in meters. \n"))

weight = int(input("Enter your weight in kilogram. \n"))

BMI = weight / (height ** height)

if BMI < 18.5:
    print("You are underweight.")
elif BMI < 24.9:
    print("You are perfectly fine")
elif BMI < 29.9:
    print("YOu are overweight. Move up.")
elif BMI < 34.9:
    print("Unfortunately you are obese!")
else:
    print("YOu are extremely obese!!!!")
