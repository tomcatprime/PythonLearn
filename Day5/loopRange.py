# for loop with range

for number in range(1, 10 ): #looping 1 - 9
    print(f"This is your number {number}")

for number in range(1, 10 + 1): #looping 1 - 10
    print(f"This is your number {number}")

# looping with step
for number in range(1, 10 + 1, 3): #looping 1 - 10
    print(f"This is your number {number}")

#loop over range and add number
total = 0
for number in range(1, 101):
    total += number
print(total)



#You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

target = int(input("type number, max 1000"))
evenSum = 0
for number in range(1, target + 1):
  if number % 2 == 0:
    evenSum += number

print(evenSum)

#or

target = int(input("type number, max 1000"))
evenSum = 0
for number in range(2, target + 1, 2):
    evenSum += number
    
print(evenSum)

