# Day 15
# Problem: Maximum Element in an Array
# Topic: Arrays / Lists
# Language: Python

# Read number of elements
num = int(input())

# Read array elements
l = []
for i in range(num):
    a = int(input())
    l.append(a)

# Find maximum element
c = max(l)

# Display result
print(f"Maximum element in the array is {c}")
