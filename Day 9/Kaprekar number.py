# Day 9
# Problem: Kaprekar Number
# Platform: HackerRank
# Topic: Python Loops / Math
# Language: Python

# Input a number
num = int(input("Enter a number: "))

# Calculate square of the number
square = num ** 2

# Count number of digits in the original number
temp = num
digits = 0
while temp > 0:
    temp //= 10
    digits += 1

# Split square into right and left parts
right = square % (10 ** digits)
left = square // (10 ** digits)

# Sum left and right parts
k = right + left

# Check if Kaprekar Number
if k == num:
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
