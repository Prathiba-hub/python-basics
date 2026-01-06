# Day 9
# Problem: Sum of Digits Till Single Digit
# Platform: HackerRank
# Topic: Python Loops / Math
# Language: Python

# Input a number
num = int(input("Enter a number: "))

# Compute sum of digits repeatedly until a single digit
temp = num
while temp >= 10:
    sum_digits = 0
    for digit in str(temp):
        sum_digits += int(digit)
    temp = sum_digits

# Print the single-digit result
print(temp)
