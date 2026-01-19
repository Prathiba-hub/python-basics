# Day 14
# Problem: Matrix Rotation (90 Degree Clockwise)
# Topic: Python Matrices
# Language: Python

# Read size of the matrix
num = int(input())

# Read matrix elements
arr = []
for i in range(num):
    arr.append(list(map(int, input().split())))

# Rotate the matrix and print the result
for i in range(num):
    for j in range(num - 1, -1, -1):
        print(arr[j][i], end=" ")
    print()
