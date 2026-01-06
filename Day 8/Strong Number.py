# Day 8
# Problem: Strong Number
# Platform: HackerRank
# Topic: Python Loops / Math
# Language: Python

import math

# Input a number
n = int(input("Enter a number: "))

# Store original number for comparison
temp = n
total = 0

# Sum the factorial of each digit
while n > 0:
    digit = n % 10
    total += math.factorial(digit)
    n //= 10

# Check if the number is a Strong Number
if temp == total:
    print("Yes")
else:
    print("No")
