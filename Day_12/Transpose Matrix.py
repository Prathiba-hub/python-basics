num=int(input())
arr=[]
for i in range(num):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(num):
    for j in range(num):
        print(arr[i][j],end=" ")
    print()
print("Transpose matrix is:")    
for i in range(num):
    for j in range(num):
        print(arr[j][i],end=" ")
    print()
