F1=int(input())
F2=int(input())
F3=int(input())
S1=int(input())
S2=int(input())
S3=int(input())
A1=int(input())
A2=int(input())
A3=int(input())
flipkart=(F1*F2/100)
val3=F1-flipkart
val4=val3+F3
flipkart=int(val4)
snapdeal=(S1*S2/100)
val5=S1-snapdeal
val6=val5+S3
snapdeal=int(val6)
amazon=(A1*A2/100)
val=A1-amazon
val2=val+A3
amazon=int(val2)
print(f"In Flipkart: Rs.{flipkart}")
print(f"In Snapdeal: Rs.{snapdeal}")
print(f"In Amazon: Rs.{amazon}")
if flipkart<snapdeal and flipkart<amazon:
    print("Choose Flipkart")
elif snapdeal<flipkart and snapdeal<amazon:
    print("Choose Snapdeal")
elif amazon<flipkart and amazon<snapdeal:
    print("Choose Amazon")
elif flipkart==snapdeal or flipkart==amazon:
    print("Choose Flipkart")
elif snapdeal==flipkart or snapdeal==amazon:
    print("Choose Snapdeal")
elif amazon==flipkart or amazon==snapdeal:
    print("Choose Amazon")
elif flipkart==amazon==snapdeal:
    print("Choose Flipkart")
