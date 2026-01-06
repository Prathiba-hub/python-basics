# Day 7
# Problem: Print Prime Numbers in a Range
# Platform: HackerRank
# Topic: Python Loops / Conditional Statements
# Language: Python

# Input the upper limit
n = int(input("Enter the upper limit: "))

# Check valid range
if 1 < n < 109:
    # Loop through numbers from 2 to n
    for num in range(2, n + 1):
        is_prime = True

        # Check if num is divisible by any number from 2 to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        # Print prime numbers
        if is_prime:
            print(num, end=" ")
