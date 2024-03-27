# List Comprehension - it is a case where we create list from othr list
# example
# new_list = [New_item for item in list]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Szejker"
letters_list = [letter for letter in name]
print(letters_list)

new_list = [n * 2 for n in range(1,5)]
print(new_list)

# list comprehension with condition
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
print(names)
list_names = [name for name in names if len(name) < 5]
print(list_names)
capital_names = [name.upper() for name in names]
print(capital_names)
short_cap_names = [name.upper() for name in names if len(name) < 5]
print(short_cap_names)