# #File not Found Error
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Sample text")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn not exist")

# #TypeError
# # text = "abc"
# # print(text + 5)

# else:
#     content = file.read()
#     print(content)

# finally:
#     file.close()
#     print("File was closed.")

#     #raising exceptions
#     raise KeyError("They key is incorrect")

height = float(input("height"))
weight = int(input("weight"))

if height > 3:
    raise ValueError("Incorrect height Value")