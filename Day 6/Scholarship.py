age=int(input())
year=int(input())
income=int(input())
arrer=int(input())
mark=float(input())
attendance=float(input())
if year>=2021 and  arrer<=2 and income<=200000 and 18<=age<=21 and mark>=60 and attendance>=80:
    print("Eligible")
elif year>=2021 and  arrer>2 and 200000<=income<=250000 and 18<=age<=21 and mark>=80 and attendance>=90:
    print("Partially Eligible")
else:
    print("Not Eligible")

    
        
    
