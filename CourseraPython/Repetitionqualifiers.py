import re
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))


print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))


print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

#exercise
#The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice.
# For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work.

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True


#exercise
#Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter,
# followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.

def check_sentence(text):
  result = re.search(r"^[A-Z][ |a-z]*[.?\!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.


#r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.


#r”/^(.+)/([^/]+)$/” This line of code matches any path and filename.



#exercise
##Question 1
# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and
# a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers,
# beginning and end-of-line characters, and character classes.
#
def check_web_address(text):
  pattern = r"^\S+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, followed by a colon, then minutes between 00 and 59
# , then an optional space, and then AM or PM, in upper or lower case.
# Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?
def check_time(text):
  pattern = r"^[1-9][0-2]?:[0-5][0-9] ?[am|pm|AM|PM]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False

# Question 3
# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses,
# with at least the first character in uppercase (if it(('s a letter), returning True if the condition is met, or False otherwise. '
# 'For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication"')
# ' should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: )
import re
def contains_acronym(text):
  pattern = r"\([A-Z1-9][a-zA-Z1-9]*\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


#
# An intern implemented a zip code checker, but it works only with five-digit zip codes. Your task is to update the checker so that it includes all nine digits of the zip code;
# the leading five digits and the optional four after the hyphen.
# The zip code needs to be preceded by at least one space, and cannot be at the start of the text. Update the regular expression.

def correct_function(text):
  result = re.search(r"[ ]\d{5}|[ ]\d{5}-\d{4}", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False