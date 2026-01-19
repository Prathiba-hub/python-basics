# Day 13
# Problem: Move all zeroes
# Topic: Python Matrices
# Language: Python

# Read number of strings
n = int(input())

# List to store strings
strings = []

# Read strings
for _ in range(n):
    strings.append(input().strip())

# Sort each string in reverse order and print
for s in strings:
    sorted_string = ''.join(sorted(s, reverse=True))
    print(sorted_string)

