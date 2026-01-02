val=int(input())
ans=(val//10)%10
if 100<=val and val<=999:
    if ans%3==0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")
