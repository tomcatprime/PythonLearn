# for loops
# for item in list_of_items:    
#    do something to each item

fruits = ["Apples", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")


# Input a Python list of student heights
student_heights = input("type inputs: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
numOfStudents = len(student_heights)
total = 0
for heigth in student_heights:
  total += heigth
avg = round(total / numOfStudents)
print(f"total height = {total}")
print(f"number of students = {numOfStudents}")
print(f"average height = {avg}")



# //largest number without max() and min()

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highestScore = 0
for score in student_scores:
  if score > highestScore:
    highestScore = score

print(f"The highest score in the class is: {highestScore}")