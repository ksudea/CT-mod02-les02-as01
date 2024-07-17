# Task 1

num1 = input("Input first number")
num2 = input("Input second number")
num3 = input("Input third number")

if num1 >= num2 and num1 >= num3:
    print( "The largest number is " + str(num1))
elif num2 >= num1 and num2 >= num3:
    print( "The largest number is " + str(num2))
else:
    print( "The largest number is " + str(num3))

# Task 2

if num1 <= num2 and num1 <= num3:
    print( "The smallest number is " + str(num1))
elif num2 <= num1 and num2 <= num3:
    print( "The smallest number is " + str(num2))
else:
    print( "The smallest number is " + str(num3))