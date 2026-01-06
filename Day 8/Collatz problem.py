# Day 8
# Problem: Collatz Problem
# Platform: HackerRank
# Topic: Python Loops / Conditional Statements
# Language: Python

# Input a number
n = int(input("Enter a number: "))

# Print the starting number
print(n)

# Initialize step counter
count = 0

# Apply Collatz sequence until n becomes 1
while n != 1:
    if n % 2 == 0:
        n = n // 2  # If even, divide by 2
    else:
        n = 3 * n + 1  # If odd, multiply by 3 and add 1
    count += 1
    print(n)

# Print total number of steps
print(count)
