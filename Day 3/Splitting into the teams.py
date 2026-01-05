# Day 3
# Problem: Splitting into the Teams
# Platform: HackerRank
# Topic: Python Basics / Arithmetic
# Language: Python

# Input total number of students and team size
n = int(input())   # Total students
n1 = int(input())  # Team size

# Calculate number of students in each team and leftover
left_out = n % n1
per_team = n // n1

# Print the result
print(f"The number of friends in each team is {per_team} and left out is {left_out}")
