#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else (-number % 10) * -1
print(f"Last digit of {number} is {last_digit} and is", end=" ")
if number > 5:
    print(f"greater than 5")
elif number == 0:
    print(f"0")
elif number < 6:
    print(f"less than 6 and not 0")
