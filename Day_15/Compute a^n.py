# Day 15
# Problem: Compute a^n (Power of a Number)
# Topic: Basic Mathematics
# Language: Python

import math

# Read base value
num = int(input())

# Read power value
num2 = int(input())

# Calculate power
ans = math.pow(num, num2)

# Display result
print(f"The value of {num} power {num2} is {int(ans)}")
