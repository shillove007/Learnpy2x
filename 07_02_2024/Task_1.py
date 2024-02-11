# Write a Python program to calculate the area of a circle given
# its radius using the formula area=π×r^2 ( Take pie as 3.14)
import math
radius = float(input("Please enter radius of circle"))
area = math.pi * pow(radius,2)
print("Area of circle you have enter is = ", area)
