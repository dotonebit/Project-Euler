"""
Project Euler - Problem 1

Find the sum of all the multiples of 3 or 5 below 1000.

See: projecteuler.net/problem=1
"""

# Variable to hold the sum.
# Start at 0.
sum = 0

# Create a for loop to iterate through numbers up to 1000.
# Write a condition to test if the number is a multiple of 3 or 5.
# If the condition is true, add the number to the sum.
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        sum += n

# Print the sum.
print(sum)
