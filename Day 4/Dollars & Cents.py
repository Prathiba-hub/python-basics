# Day 4
# Problem: Dollars & Cents
# Platform: HackerRank
# Topic: Python Basics / Arithmetic
# Language: Python

# Input dollars and cents
d1 = int(input())
c1 = int(input())
d2 = int(input())
c2 = int(input())

# Add dollars and cents
total_dollars = d1 + d2
total_cents = c1 + c2

# Convert excess cents to dollars
if total_cents >= 100:
    total_cents -= 100
    total_dollars += 1

# Output result
print(total_dollars)
print(total_cents)
