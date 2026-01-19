# Day 14
# Problem: Number of Digits
# Topic: Recursion
# Language: Python

def count_num(n):
    # Base case: single digit
    if n < 10:
        return 1
    else:
        # Recursive call
        return 1 + count_num(n // 10)

# Read input from user
num = int(input())

# Count number of digits
dig = count_num(num)

# Display result
print(f"The number of digits in {num} is {dig}")
