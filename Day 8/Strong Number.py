import math
n=int(input())
temp=n
s=0
while n>0:
    f=n%10
    s+=math.factorial(f)
    n//=10
if temp==s:
    print("Yes")
else:
    print("No")
