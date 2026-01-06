# Day 4
# Problem: Reverse a 3-Digit Number
# Platform: HackerRank
# Topic: Python Basics / Strings
# Language: Python

num = int(input())

# Convert number to string
val = str(num)

# Reverse the number using string slicing
reversed_num = val[::-1]

# Print reversed number
print(int(reversed_num))
