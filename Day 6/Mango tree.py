row=int(input())
col=int(input())
tree=int(input())
if tree<=col:
    print("Yes")
elif tree%col==1:
    print("Yes")
elif tree%col==0:
    print("Yes")
else:
    print("No")
