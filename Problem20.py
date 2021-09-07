"""
Project Euler - Problem 20

Find the sum of digits in the number 100!

See: projecteuler.net/problem=20
"""

# Import the math library to use factorial().
import math

# Variable to hold the result for 100!
hundred = math.factorial(100)

# Variable for the sum of digits in 100!
# Start at 0.
sum = 0

# Loop to iterate through the digits in hundred.
# Add each digit to sum.
# Convert between integers and strings using str() and int().
for digit in str(hundred):
    sum += int(digit)

# Print the result of sum.
print(str(sum))
