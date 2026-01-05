n=int(input())
left_half=1
right_half=(n**2)+1
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print("--",end="")
    for k in range(1,i+1):
        print(left_half,end="*")
        left_half+=1
    for l in range(1,i+1):
        print(right_half,end="")
        if l<i:
            print("*",end="")
        right_half+=1
    print()
    right_half=right_half-(i-1)*2-1

    
