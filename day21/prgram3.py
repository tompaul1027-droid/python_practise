def robot(a):
    if(a=="forward"):
        print("i am moving forward")
    elif(a=="left"):
        print("going left")
    elif(a=="right"):
        print("going right")
    else:
        print("going backwords")
        
i=0
while i==0:
    a=input("Enter the word:")
    robot(a)
        