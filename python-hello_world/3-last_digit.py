#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 0:
    number = str(number)
    last_digit = (number[-1])
    if int(last_digit) > 5:
        print("Last digit of {} is {} and is greater than 5".format(number,last_digit))
    elif int(last_digit) < 6 and int(last_digit) != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,last_digit))
    elif last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number,last_digit))
elif number < 0:
    number = str(number)
    last_digit = (number[-1])
    last_digit = -(int(last_digit))
    if last_digit < 6 and last_digit != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,last_digit))
    elif last_digit == 0:
        print("Last digit of {} is {} and is 0".format(number,last_digit))
else:
    number = str(number)
    last_digit = (number[-1])
    print("Last digit of {} is {} and is 0".format(number,last_digit))