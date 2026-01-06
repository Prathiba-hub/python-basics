# Day 6
# Problem: Mango Tree
# Platform: HackerRank
# Topic: Python Conditional Statements / Arithmetic
# Language: Python

# Input number of rows, columns, and trees
rows = int(input())
cols = int(input())
trees = int(input())

# Check if trees can be arranged properly
if trees <= cols:
    print("Yes")
elif trees % cols == 0 or trees % cols == 1:
    print("Yes")
else:
    print("No")
