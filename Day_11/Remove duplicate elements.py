# Day 11
# Problem: Remove Duplicate Elements
# Platform: HackerRank
# Topic: Python Lists / Sets
# Language: Python

# Input number of elements
num = int(input("Enter number of elements: "))

# Input array elements
arr = []
for _ in range(num):
    arr.append(int(input()))

# Remove duplicates while preserving order
unique_arr = []
seen = set()

for item in arr:
    if item not in seen:
        seen.add(item)
        unique_arr.append(item)

# Output result
for element in unique_arr:
    print(element)
