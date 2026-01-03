n=int(input())
m=int(input())
for i in range(n,m+1):
    last=i%10
    first=i//10
    sum1=first+last
    product=first*last
    sum2=sum1+product
    if sum2==i:
        print(i,end="\n")
