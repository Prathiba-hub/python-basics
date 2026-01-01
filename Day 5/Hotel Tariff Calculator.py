month=int(input())
month=abs(month)
rent=int(input())
rent=abs(rent)
day=int(input())
day=abs(day)
if month<=12 and month !=0:
    if month==4 or month==5 or month==6 or month==11 or month==12:
        rent1=rent*(20/100)
        rent2=rent+rent1
        amt=rent2*day
        print(int(amt))
    else:
            amt1=rent*day
            print(int(amt1))
else:
    print("Invalid Input")
