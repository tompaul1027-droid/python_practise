a=int(input("Enter the number:"))
x=0
for i in range(a):
    if(i%4==0):
        print("*")
    elif(i%4==1):
        print("**")
    elif(i%4==2):
        print("***")
    else:
        print("****")

    