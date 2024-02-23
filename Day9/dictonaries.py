#dictonaries key - value

#{key: value}
programming_dict = {
    "Bug": "This is description of bug",
    "Function": "A piece of code that you can easily call over and over again",
    }

# retrieve item from dictionary - ex. retrieve bug
programming_dict["Bug"]


# adding new item to dictonary
programming_dict["Loop"] = "The action of doing something over and over again"
print(programming_dict)

#creaty an empty dictionary
empty_dictionary = {}

# edit item in dictionary
programming_dict["Bug"] = "A moth in your computer"
print(programming_dict)


# loop through dictionary
for key in programming_dict:
    print(key) #will print only key
    print(programming_dict[key]) #will print value of the key




#wipe an exiting dictionary

programming_dict = {}
print(programming_dict)