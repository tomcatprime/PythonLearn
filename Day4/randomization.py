#randomization 

import random
import my_module #importing own module with PI number
#generate random integer

randomNum = random.randint(1,10) # in () - range


print(randomNum)
print(my_module.pi)

multiply = randomNum * my_module.pi
print(multiply)

# random float number
randomFloat = random.random() # between 0.00000000 - 0.99999999
print(f"this is random float {randomFloat}")

#generate float number between 0 -5
randomFloatNew = random.random() * 5 #multiply by 5
print(F"This is new random float between 0-5 {randomFloatNew}")

# tails or heads
randomSide = random.randint(0,1)
if randomSide == 1:
  side = "heads"
  print(side.capitalize())
else:
  side = "tails"
  print(side.capitalize())

  