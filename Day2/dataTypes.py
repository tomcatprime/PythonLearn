# len() - count number of characters of string
# string  - characters - e.x - "Hello Here"

#pull out character of string - called subscript
name = "Karol"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[0:3]) #from position 0 to 2

# Integer - just write number without any "" or ''
print(123213)
justinteger = 123124

print("Abbey"[4])

#Float - number with decimal
num = 3.283217

# Boolean

a = True
b = False

if a > b:
    print("True is greater than False")

num_char = len(input("Type anyything: "))
print(num_char)
print(type(num_char))

# conversion from int to string
newNumChar = str(num_char)
print(newNumChar)
print(type(newNumChar))


two_digit_number = input("Type 2 digit number: ")
firstNumber = int(two_digit_number[0])
secondNumber = int(two_digit_number[1])

result = firstNumber + secondNumber
print(result)

# mathematical operations

print(126 + 126)
print(100-50)
print(2*2)
print(100/4) #when dividing, all the time ending up with float number
2 ** 3 # power of = equals to 2 * 2 * 2


