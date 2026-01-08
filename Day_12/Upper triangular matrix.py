num=int(input())
arr=[]
for _ in range(num):
    l=list(map(int,input().split()))
    arr.append(l)
utm=True
for i in range(num):
    for j in range(i):
        if arr[i][j]!=0:
            utm=False
if utm==True:
    print("Upper triangular matrix")
else:
    print("Not an Upper triangular matrix")
            
        
