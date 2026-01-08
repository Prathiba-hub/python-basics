# Day 12
# Problem: Maximum Element in Each Column
# Topic: Python Matrices
# Language: Python

# Input matrix dimensions
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

# Input matrix
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Find and print maximum element in each column
for col in range(m):
    max_value = matrix[0][col]
    for row in range(1, n):
        if matrix[row][col] > max_value:
            max_value = matrix[row][col]
    print(max_value)
