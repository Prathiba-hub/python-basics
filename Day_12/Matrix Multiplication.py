num1,num2=map(int,input().split())
arr1=[]
for i in range(num1):
    l=list(map(int,input().split()))
    arr1.append(l)
arr2=[]
for i in range(num2):
    l=list(map(int,input().split()))
    arr2.append(l)
mul=[[0]*num2 for j in range(num2)]
for i in range(num1):
        for j in range(num2):
            for k in range(num2):
                mul[i][j] += arr1[i][k] * arr2[k][j]
for m in mul:
    print(' '.join(map(str,m)))
