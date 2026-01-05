num=int(input())
num_str=str(num)
m=0
for i in num_str:
    digit=int(i)
    m=m+digit
    n=m//10#44//10=4
    first=m%10
    A=n+first
print(A)
 

    
