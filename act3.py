# Square Root Calculator Project

import math

print("SQUARE ROOT CALCULATOR\n")

# Taking input from the user
number = float(input("Enter a number to find its square root: "))

# Checking if the number is positive
if number >= 0:
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")
else:
    print("Square root of a negative number is not defined for real numbers.")
