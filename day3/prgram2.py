a=int(input("Enter the number:"))
x=0
for i in range(a):
    if(i%3==0):
        x=x+2
        print(x)
    elif(i%3==1):
        x=x+3
        print(x)
    else:
        x=x+5
        print(x)
