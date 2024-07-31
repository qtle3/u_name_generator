# This program generates username from specified first name and last name
import random

# set to store usernames
usernames = set()


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

    # check if username is already in use
    if uname not in usernames:
        # add username to set
        usernames.add(uname)
        print("Username is available")
    else:
        print("Username is not available")
        generate_uname()


generate_uname()
