#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    LastDigit = number % 10
else:
    LastDigit = ((number * -1) % 10) * -1

string1 = "Last digit of %d is %d and is" % (number, LastDigit)

if LastDigit == 0:
    print(string1, "0")
elif LastDigit > 5:
    print(string1, "greater than 5")
else:
    print(string1, "less than 6 and not 0")
