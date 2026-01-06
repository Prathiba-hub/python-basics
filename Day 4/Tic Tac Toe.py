# Day 4
# Problem: Tic Tac Toe
# Platform: HackerRank
# Topic: Python Conditional Statements
# Language: Python

n = int(input())

if 1 <= n <= 9:
    if n == 1:
        print("0 0")
    elif n == 2:
        print("0 1")
    elif n == 3:
        print("0 2")
    elif n == 4:
        print("1 0")
    elif n == 5:
        print("1 1")
    elif n == 6:
        print("1 2")
    elif n == 7:
        print("2 0")
    elif n == 8:
        print("2 1")
    elif n == 9:
        print("2 2")
