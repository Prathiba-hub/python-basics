# Day 12
# Problem: Upper Triangular Matrix
# Topic: Python Matrices
# Language: Python

# Input size of square matrix
n = int(input("Enter the size of the matrix: "))

# Input matrix
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Check if matrix is upper triangular
is_upper_triangular = True
for i in range(n):
    for j in range(i):
        if matrix[i][j] != 0:
            is_upper_triangular = False
            break

# Output result
if is_upper_triangular:
    print("Upper triangular matrix")
else:
    print("Not an Upper triangular matrix")
