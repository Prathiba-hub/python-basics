# Day 13
# Problem: Uniformity Matrix
# Topic: Python Matrices
# Language: Python

n = int(input())
matrix = []

# Reading the matrix
for _ in range(n):
    matrix.append(list(map(int, input().split())))

even_count = 0
odd_count = 0

# Counting even and odd elements
for i in range(n):
    for j in range(n):
        if matrix[i][j] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

# Checking uniformity
if even_count == n * n or odd_count == n * n:
    print("Yes")
else:
    print("No")
