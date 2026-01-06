# Day 5
# Problem: Electricity Bill
# Platform: HackerRank
# Topic: Python Conditional Statements / Arithmetic
# Language: Python

# Input electricity units consumed
unit = int(input())

# Calculate bill based on unit slabs
if unit <= 200:
    money = unit * 0.5
elif unit <= 400:
    money = (unit * 0.65) + 100
elif unit <= 600:
    money = (unit * 0.80) + 200
else:
    money = (unit * 1.25) + 425

# Convert to integer and print
money = int(money)
print(f"Rs.{money}")
