# Day 14
# Problem: Sum of Array Elements
# Topic: Arrays / Lists
# Language: Python

# Read number of elements
num = int(input())

# Read array elements
l = []
for i in range(num):
    a = int(input())
    l.append(a)

# Calculate sum of array elements
add = sum(l)

# Display result
print(add)
