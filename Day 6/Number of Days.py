year=int(input())
month=int(input())
val=[1,3,5,7,8,10,12]
val2=[4,6,9,11]
if 1900<=year<=9999 and 1<=month<=12:
    if month in val:
        print("31 Days")
    if month==2:
        if year%4==0 and year%100!=0 or year%400==0:
            print("29 Days")
        else:
            print("28 Days")
    if month in val2:
        print("30 Days")
else:
    print("0")
