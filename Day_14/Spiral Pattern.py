n = int(input())#4
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
top, bottom = 0, n - 1
left, right = 0, n - 1
result = []
while top <= bottom and left <= right:#t=0: b=3 : l=0: r=3
    for i in range(left, right + 1):
        result.append(matrix[top][i])#1 2 3 4 #top is the current top row index 
    top += 1
    for i in range(top, bottom + 1):#1 to 4
        result.append(matrix[i][right])#8 12 16 #right is column index
        
    right -= 1 
    if top <= bottom:
        for i in range(right, left - 1, -1):#3 to -1 decrementing 
            result.append(matrix[bottom][i])#15 14 13
        
        bottom -= 1#2
    if left <= right:
        for i in range(bottom, top - 1, -1): #
            result.append(matrix[i][left])#9,5
        left += 1


print(" ".join(map(str,result)))
