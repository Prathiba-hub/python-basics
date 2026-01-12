# Day 10
# Problem: Sum of Even and Odd Numbers
# Platform: HackerRank
# Topic: Python Lists / Loops
# Language: Python

# Input number of elements
num = int(input("Enter the number of elements: "))

# Input array elements
arr = []
for _ in range(num):
    arr.append(int(input()))

# Separate even and odd numbers
even = []
odd = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# Calculate sums
sum_even = sum(even)
sum_odd = sum(odd)

# Print results
print(f"The sum of the even numbers in the array is {sum_even}")
print(f"The sum of the odd numbers in the array is {sum_odd}")
