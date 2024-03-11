# file = open("text.txt")

# content = file.read()

# print(content)

# file.close()

# other way

with open("text.txt", mode="a") as file:
    contents = file.read()
    print(contents)


with open("new_file.txt", mode="w")as new_file:
    new_file.write("New file and new text")