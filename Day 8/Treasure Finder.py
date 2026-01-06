# Day 8
# Problem: Treasure Finder
# Platform: HackerRank
# Topic: Python Math / Lists
# Language: Python

import math

# Input numbers on the three boxes
box1 = int(input("Enter number on box 1: "))
box2 = int(input("Enter number on box 2: "))
box3 = int(input("Enter number on box 3: "))

# Find the box with the median number (the treasure)
boxes = [box1, box2, box3]
boxes.sort()
treasure_box = boxes[1]  # Median value
print(f"The treasure is in the box which has the number {treasure_box}")

# Calculate the code to open the box (GCD of the three numbers)
code = math.gcd(math.gcd(box1, box2), box3)
print(f"The code to open the box is {code}")
