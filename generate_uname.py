# This program generates username from specified first name and last name
import random


def generate_uname():
    # get user’s first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")
    # generate a random number between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = num1 + num2
    num = str(num1) + str(num2) + str(num3)
    # concatenate first initial with 7 chars of last name
    uname = first[0] + last[:7] + num
    print("uname =", uname)


generate_uname()
