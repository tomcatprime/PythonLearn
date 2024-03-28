import pandas

student_dict = {
    "student": ["Angela", "Szejker", "James"],
    "score": [56, 76, 98]
}
# creating data frame
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print("#############################")
# loop through data frame
# pandas has bulti in loop method
for (index, row) in student_data_frame.iterrows():
    print(index)
    print("#############################")
    print(row)
    print("#############################")
    print(row.score)
    if row.student == "Angela":
        print(row.score)
