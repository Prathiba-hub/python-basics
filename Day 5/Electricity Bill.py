unit=int(input())
if(unit<=200):
    money=unit*0.5
    money=int(money)
    print(f"Rs.{money}")
elif(unit>200 and unit<=400):
    money=(unit*0.65)+100
    money=int(money)
    print(f"Rs.{money}")
elif(unit>400 and unit<=600):
    money=(unit*0.80)+200
    money=int(money)
    print(f"Rs.{money}")
else:
    money=(unit*1.25)+425
    money=int(money)
    print(f"Rs.{money}")
