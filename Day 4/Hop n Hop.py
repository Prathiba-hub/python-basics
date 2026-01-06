# Day 4
# Problem: Hop n Hop
# Platform: HackerRank
# Topic: Python Math
# Language: Python

import math

# Input coordinates
x = int(input())
y = int(input())

# Fixed point coordinates
x1, y1 = 3, 4

# Calculate distance using distance formula
distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

# Print integer part of the distance
print(int(distance))
