# Day 10
# Problem: Count Distinct Elements
# Platform: HackerRank
# Topic: Python Lists / Sets
# Language: Python

# Input the number of elements
num = int(input("Enter the number of elements in the array: "))

# Input array elements
arr = []
for _ in range(num):
    arr.append(int(input()))

# Use a set to find distinct elements
distinct_elements = set(arr)

# Print the count of distinct elements
print(f"There are {len(distinct_elements)} distinct elements in the array.")
