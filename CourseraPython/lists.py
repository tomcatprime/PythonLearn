multiples = []
for x in range(1, 11):
    multiples.append(x*7)


print(multiples)

multiples1 = [x*7 for x in range(1,11)]
print(multiples1)

#list comprehension
languages = ["python", "perl", "c"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)


#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.
def odd_numbers(n):
	return [x for x in range(0, n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


def squares(start, end):
    return [n*n for n in range(start, end + 1)] 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block. 

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

