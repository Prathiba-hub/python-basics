# Day 7
# Problem: Special Number
# Platform: HackerRank
# Topic: Python Loops / Arithmetic
# Language: Python

# Input range
n = int(input("Enter the starting number: "))
m = int(input("Enter the ending number: "))

# Loop through numbers in the range
for num in range(n, m + 1):
    first_digit = num // 10
    last_digit = num % 10

    sum_digits = first_digit + last_digit
    product_digits = first_digit * last_digit
    total = sum_digits + product_digits

    # Check if the number is a Special Number
    if total == num:
        print(num)
