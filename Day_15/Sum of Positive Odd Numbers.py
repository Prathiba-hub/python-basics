# Day 15
# Problem: Sum of Positive Odd Numbers
# Topic: Recursion / Arrays
# Language: Python

def cal_sum(o_arr):
    # Base case: empty list
    if len(o_arr) == 0:
        return 0
    else:
        # Recursive sum
        return o_arr[0] + cal_sum(o_arr[1:])

# Read number of elements
n = int(input())

# Read array elements
arr = []
for i in range(n):
    arr.append(int(input()))

# Filter positive odd numbers
odd_arr = []
for i in arr:
    if i % 2 != 0 and i > 0:
        odd_arr.append(i)

# Calculate sum of positive odd numbers
s = cal_sum(odd_arr)

# Display result
print(f"Sum = {s}")
