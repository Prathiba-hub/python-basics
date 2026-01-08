# Day 12
# Problem: Matrix Multiplication
# Topic: Python Matrices
# Language: Python

# Input dimensions
r1, c1 = map(int, input("Enter rows and columns of first matrix: ").split())
r2, c2 = map(int, input("Enter rows and columns of second matrix: ").split())

# Input first matrix
mat1 = []
for _ in range(r1):
    mat1.append(list(map(int, input().split())))

# Input second matrix
mat2 = []
for _ in range(r2):
    mat2.append(list(map(int, input().split())))

# Check if multiplication is possible
if c1 != r2:
    print("Matrix multiplication not possible")
else:
    # Initialize result matrix with zeros
    result = [[0 for _ in range(c2)] for _ in range(r1)]

    # Matrix multiplication logic
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    # Print result matrix
    for row in result:
        print(" ".join(map(str, row)))
