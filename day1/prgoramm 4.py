a=int(input("number1:"))
b=int(input("number2:"))
c=input("enter the operation:")
print(type(c))
if(c=="+"):
    print("sum:",a+b)
elif(c=="-"):
    print("difference:",a-b)
elif(c=="*"):
    print("product:",a*b)
elif(c=="/" or c=="%"):
    if(b!=0):
        print("quotient:",a/b)
        print("remainder:",a%b)
    else:
        print("invalid input")    
else:
    print("invalid operator")