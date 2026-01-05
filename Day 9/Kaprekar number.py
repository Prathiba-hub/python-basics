n=int(input())
s=n**2
num=n
sum=0
while n>0:
    n=n//10
    sum+=1
right=s%(10**sum)
left=s//(10**sum)
k=right+left   
if k==num:
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
