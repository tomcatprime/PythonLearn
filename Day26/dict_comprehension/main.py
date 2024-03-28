# new_dict = {new_key:new_value for item in list}

# or
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# random scores
students = {student:random.randint(1,100) for student in names}
print(students)

passed_students = {student:score for (student, score) in students.items() if score >= 60}
print(passed_students)


# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

# Try Googling to find out how to convert a sentence into a list of words.

# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇

strings = sentence.split()

a = {item:len(item) for item in strings}

print(a)


# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f use this formula:

# (temp_c * 9/5) + 32 = temp_f

temps ={"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# (temp_c * 9/5) + 32 = temp_f

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}


print(weather_f)