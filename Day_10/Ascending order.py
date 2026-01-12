# Day 10
# Problem: Ascending Order
# Platform: HackerRank
# Topic: Python Lists / Sorting
# Language: Python

# Input size of the array
num = int(input("Enter the number of elements: "))

# Input array elements
arr = []
for _ in range(num):
    arr.append(int(input()))

# Sort the array in ascending order
arr.sort()

# Print the sorted array
print("The Sorted array is:")
for elem in arr:
    print(elem)
