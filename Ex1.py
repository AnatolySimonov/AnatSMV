birth_year = int(input("Enter your birth year"))
required_year = int(input("Enter required year"))
MAX_BY = 2021
MIN_BY = 1900
MAX_RY = 2150
MIN_RY = 2022
if MAX_BY >= birth_year >= MIN_BY and MAX_RY >= required_year >= MIN_RY:
    age = required_year - birth_year
    print("In", required_year, "you'll be", age, "years old")
else:
    print("Error. Enter correct information")
