n=int(input())
if 1<n<109:
    for n in range(2,n+1):
        flag=True
        if n<2:
            continue
        if n==2:
            print("2",end=" ")
            continue
        for i in range(2,n):
            if n%i==0:
                flag=False
                break
        if flag:
            print(n,end=" ")
