# Day 9
# Problem: Same or Not
# Platform: HackerRank
# Topic: Python Lists / Conditional Statements
# Language: Python

# Input size and elements of first list
arr1 = []
val1 = int(input("Enter number of elements in first list: "))
for _ in range(val1):
    arr1.append(int(input()))

# Input size and elements of second list
arr2 = []
val2 = int(input("Enter number of elements in second list: "))
for _ in range(val2):
    arr2.append(int(input()))

# Compare sum and length of the two lists
if sum(arr1) == sum(arr2) and len(arr1) == len(arr2):
    print("Same")
else:
    print("Not Same")
