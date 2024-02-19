#write program that will print from 1 too 100, if number is divisible by 3, will print fizz instead of number
# if divisble by 5, will print Buzz instead of number
# if divisible by 3 and 5 will print FizzBuzz

target = 100
for number in range(1,target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)