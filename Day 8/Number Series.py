num=int(input())
for i in range(1,num+1):
    if i%2==0:
        ans=(i**2)-2
    else:
        ans=(i**2)-1
    print(ans,end=" ")
