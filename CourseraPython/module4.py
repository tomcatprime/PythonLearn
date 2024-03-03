def first_character(string):
    # Complete the return statement using a string operation.
    return string[:1]


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K

def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word, word.upper())

print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"


#Question 4
#Fill in the blank to complete the “increments” function. This function should use a list comprehension to create a list of numbers incremented by 2 (n+2). 
#The function receives two variables and should return a list of incremented consecutive numbers between “start” and “end” inclusively (meaning the range should include both the “start” and “end” values). 
#Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 5]”.

def squares(start, end):
	return [ num**2 for num in range(start, end+1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



#Fill in the blanks to complete the “endangered_animals” function. This function accepts a dictionary containing a list of endangered animals (keys) and their remaining population (values).
# For each key in the given “animal_dict” dictionary, format a string to print the name of the animal, with one animal name per line.


def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for key in animal_dict:

        # Use a string method to format the required string.
        result += "{}".format(key) + "\n"
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger



def combine_guests(guests1, guests2):
  list1 = guests1 # Use a dictionary method to combine the dictionaries.
  list2 = guests2

  list2.update(list1)
  return list2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}



def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook = {} 
    # Complete the for loop to iterate over the new gradebook. 
    for key in old_gradebook.keys():
      # Use a dictionary operation to reset the grade values to 0.
      new_gradebook[key] = 0

    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}



