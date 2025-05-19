# I Import the Math module to use the power function and the log2 function.
import math

# Prompts the user to enter a number x.
x = int(input("Enter a number 'x': "))

# Prompts the user to enter a number y.
y = int(input("Enter a number 'y': "))

# Prints the number x raised to the power y. Using the Power function.
print(f'x raised to the power y: {math.pow(x, y)}')

# Prints the log2 of the number x
print(f'The log (base 2) of x: {math.log2(x)}')
