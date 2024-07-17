# Task 1

year = int(input("Please input a valid year: "))

if year % 400 == 0:
    print("True: this is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("True: this is a leap year")
else:
    print("False: this is not a leap year")