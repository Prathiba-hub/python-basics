arr=[]
num=int(input())
for i in range(num):
    arr.append(int(input()))
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
add1=sum(even)
add2=sum(odd)
print(f"The sum of the even numbers in the array is {add1}")
print(f"The sum of the odd numbers in the array is {add2}")

        
