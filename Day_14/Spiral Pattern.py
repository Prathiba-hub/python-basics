# Day 14
# Problem: Spiral Pattern (Spiral Matrix Traversal)
# Topic: Python Matrices
# Language: Python

# Read size of the matrix
n = int(input())

# Read matrix elements
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

# Initialize boundaries
top, bottom = 0, n - 1
left, right = 0, n - 1

# List to store spiral order
result = []

# Traverse the matrix in spiral order
while top <= bottom and left <= right:

    # Traverse top row
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    # Traverse right column
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    # Traverse bottom row
    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    # Traverse left column
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

# Print spiral order
print(" ".join(map(str, result)))
