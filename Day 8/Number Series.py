# Day 8
# Problem: Number Series
# Platform: HackerRank
# Topic: Python Loops / Arithmetic
# Language: Python

# Input the number of terms
num = int(input("Enter the number of terms: "))

# Generate the series
for i in range(1, num + 1):
    if i % 2 == 0:
        ans = (i ** 2) - 2  # Even term formula
    else:
        ans = (i ** 2) - 1  # Odd term formula
    print(ans, end=" ")
