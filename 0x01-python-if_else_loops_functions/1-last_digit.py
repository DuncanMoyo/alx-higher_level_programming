#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
else:
    last_digit = number % -10
opening = "Last digit of"
greater = "and is greater than 5"
less = "and is less than 6 and not 0"
if last_digit > 5:
    print("{} {} is {} {}".format(opening, number, last_digit, greater))
elif last_digit == 0:
    print("{} {} is {} and is 0".format(opening, number, last_digit))
else:
    print("{} {} is {} {}".format(opening, number, last_digit, less))
