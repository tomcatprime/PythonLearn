filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for file in filenames:
    if file.endswith(".hpp"):
        new_file = file.replace(".hpp", ".h")
        newfilenames.append(new_file)
    else:
        newfilenames.append(file)
print(filenames)
print(newfilenames)
    
        
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
    # Create the pig latin word and add it to the list
  pigText = ""
  for word in words:
      char = (word[0])
      new_word = word[1:]
      final_word = new_word + char + "ay "
      pigText += final_word

  print(pigText)     

# Turn the list back into a phrase
  return text
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


def group_list(group, users):
  members = ", ".join(users)
  return group + ": " + members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"




def guest_list(guests):
	for guess in guests:
         name = guess[0]
         age = guess[1]
         title = guess[2]
         print("{a} is {b} years old and works as {c}".format(a = name, b = age, c = title))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""