# Day 11
# Problem: Array Insertion
# Platform: HackerRank
# Topic: Python Lists
# Language: Python

# Input number of elements
num = int(input("Enter number of elements: "))

# Input array elements
arr = []
for _ in range(num):
    arr.append(int(input()))

# Input position
pos = int(input("Enter the position to insert: "))

# Validate position
if 1 <= pos <= len(arr):
    val = int(input("Enter the value to insert: "))
    arr.insert(pos - 1, val)

    print("Array after insertion is")
    for element in arr:
        print(element)
else:
    print("Invalid Input")
