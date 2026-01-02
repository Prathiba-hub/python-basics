day1=int(input())
day2=int(input())
day3=int(input())
day4=int(input())
day5=int(input())
day6=int(input())
day7=int(input())
week=day2+day3+day4+day5+day6
sal=week*100
if day2>8:
    sal+=(day2-8)*15
if day3>8:
    sal+=(day3-8)*15
if day4>8:
    sal+=(day4-8)*15
if day5>8:
    sal+=(day5-8)*15
if day6>8:
    sal+=(day6-8)*15
if week>40:
    sal+=(week-40)*25
if day7>0:
    bon=int(day7*0.25*100)
    sal+=(bon)+(day7*100)
if day1>0:
    bon=int(day1*0.50*100)
    sal+=(bon)+(day1*100)
print(sal)
    

    

