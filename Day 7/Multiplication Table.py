# Day 7
# Problem: Multiplication Table
# Platform: HackerRank
# Topic: Python Loops / Arithmetic
# Language: Python

# Input the number and range
n = int(input("Enter n: "))
m = int(input("Enter m: "))

# Print multiplication table
print(f"The multiplication table of {n} is:")
for i in range(1, m + 1):
    print(f"{i} * {n} = {i * n}")
