n=int(input())
m=int(input())
arr=[]
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
for i in range(m):
    maxi=arr[0][i]
    for j in range(1,n):
        if arr[j][i]>maxi:
            maxi=arr[j][i]
    print(maxi)
        
        
    
        
