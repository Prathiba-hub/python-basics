# Day 3
# Problem: 3 Psychos
# Platform: HackerRank
# Topic: Python Basics / Arithmetic
# Language: Python

# Input values
a = int(input())  # Quantity
b = int(input())  # Selling price per unit
c = int(input())  # Cost price per unit

# Calculate total selling price and total cost price
total_sp = a * b
total_cp = a * c

# Calculate profit or loss
profit_loss = total_sp - total_cp

# Print final profit/loss after some adjustment (100)
print(profit_loss - 100)
