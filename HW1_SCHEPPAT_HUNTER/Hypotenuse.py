# description: calculate the hypotenuse of a triangle given two numbers
# author: SCHEPPAT, Hunter
# date: 9.7.2022

import math

print("This program calculates the hypotenuse of a right triangle")

# get the base and height of the triangle
base = float(input("Enter the base of a triangle: "))
height = float(input("Enter the height of a triangle: "))

# calculate and print the hypotenuse
hypotenuse = round(math.sqrt((base**2) + (height**2)),2)
print("the hypotenuse is " + str(hypotenuse))
