#   Create a program that takes two numbers as input and prints whether
#   the first number is greater than, less than, or equal to the second number.

#   takes two inputs from user.
number1 = int(input("Enter the first number\n "))
number2 = int(input("Enter the second number \n "))

if number1 > number2:
    print("First number is greater than second number")
elif number1 < number2:
    print("First number is less than second number")
else:
    print("First number is equal to the second number")
