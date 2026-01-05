# Day 3
# Problem: Debt Repay
# Platform: HackerRank
# Topic: Python Basics / Arithmetic
# Language: Python

# Input principal, interest rate, and years
p = float(input())  # Principal
i = float(input())  # Interest rate (annual)
y = float(input())  # Number of years

# Calculate simple interest
ins = (p * i * y) / 100
print(f"{ins:.2f}")  # Print interest with 2 decimal places

# Calculate total amount after adding interest
amt = p + ins
print(f"{amt:.2f}")

# Calculate discount on interest (2%)
dic = ins * 2 / 100
print(f"{dic:.2f}")

# Calculate final amount after discount
fin = amt - dic
print(f"{fin:.2f}")
