# Day 12
# Problem: Transpose Matrix
# Topic: Python Matrices
# Language: Python

# Input size of square matrix
n = int(input("Enter the size of the matrix: "))

# Input matrix
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# Print original matrix
print("Original Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

# Print transpose matrix
print("Transpose matrix is:")
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()
