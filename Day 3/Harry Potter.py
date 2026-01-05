# Day 3
# Problem: Sum of First and Last Digit
# Platform: HackerRank
# Topic: Python Basics / Math
# Language: Python

import math

# Input a number
n = int(input())

# Take absolute value to handle negative numbers
val = abs(n)

# Extract first digit (thousands place)
first = val // 1000

# Extract last digit (units place)
last = val % 10

# Print the sum of first and last digit
print(first + last)
