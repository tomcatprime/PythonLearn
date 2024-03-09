# reading csv files

import csv
# f = open("csv_file.txt")
# csv_f = csv.reader(f)
# for row in csv_f:
#     name, phone, role = row
#     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# f.close()

# generating csv
hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
    
    
# generating csv filr by using dictionaries

users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    
    
# reading file with dicionaries
#the follow command should be used in the terminal
cat software.csv 
#Output name,version,status,users
#MailTree,5.34,production,324
#CalDoor,1.25.1,beta,22
#Chatty Chicken,0.34,alpha,4
with open('software.csv') as software:
reader = csv.DictReader(software)
     for row in reader:
print(("{} has {} users").format(row["name"], row["users"]))






# exercise:
import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename)as filenames:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(filenames)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))







import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, 'r') as f:
    # Read the rows of the file
    rows = csv.reader(f)
    next(rows)
    # Process each row
    for row in rows:
      name, color, type = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(color, name, type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))