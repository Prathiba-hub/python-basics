# Day 12
# Problem: Smallest Positive Missing Number
# Topic: Python Arrays
# Language: Python

# Input number of elements
n = int(input("Enter number of elements: "))

# Input array elements
arr = list(map(int, input().split()))

# Filter only positive numbers
positive_numbers = [num for num in arr if num > 0]

# Sort positive numbers
positive_numbers.sort()

# Find smallest missing positive number
smallest_missing = 1
for num in positive_numbers:
    if num == smallest_missing:
        smallest_missing += 1

# Output result
print(smallest_missing)
