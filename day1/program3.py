#leapyear
a=int(input("enter a year"))
print(type(a))
if((a%4==0 and a%100!=0) or (a%400==0)):
    print("its a leap  year")
else:
    print("its not leap year")