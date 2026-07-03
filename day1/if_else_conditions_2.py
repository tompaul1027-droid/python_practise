#largest of 3 
a=int(input("number1:"))
b=int(input("number2:"))
c=int(input("number3:"))
if(a>b and a>c):
    print('nummber1 is the largest ')
elif(b>a and b>c):
    print("number2 is the largest")
elif(a==b or a==c or b==c): 
    if(a==b==c):
        print("all the numbers are equal")
    elif(a==b):     
        print("num1 and num2 are equal")
    elif(b==c):
        print("num2 and num3 are equal")
    elif(a==c):
         print("num1 and num3 are equal")
             
else:
    print("number3 is the largest")
