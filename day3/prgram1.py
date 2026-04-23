a=int(input("Enter the number:"))
x=0
for i in range(a):
    if(i%2==0):
        x=x+2
        print(x)
    else:
        x=x+3
        print(x)
    