n=int(input())
print(n)
count=0
while n!=1:
    if n%2==0:
        count+=1
        n=n//2
        print(n)
    else:
        count+=1
        n=(3*n)+1
        print(n)
print(count)
    
    
