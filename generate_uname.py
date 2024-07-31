# This program generates username from specified first name and last name

def generate_uname() :
    # get user’s first and last names
   first = input("Please enter your first name (all lowercase): ")
   last = input("Please enter your last name (all lowercase): ")

   # concatenate first initial with 7 chars of last name
   uname = first[0] + last[:7]
   print("uname =",uname)

generate_uname()
