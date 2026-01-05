import math
box1=int(input())
box2=int(input())
box3=int(input())
l=[box1,box2,box3]
l.sort()
l=l[1]
print(f"The treasure is in the box which has the number {l}")
code1=math.gcd(math.gcd(box1,box2),box3)
print(f"The code to open the box is {code1}")
