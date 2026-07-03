def battery(a):
    if(a>=70 and a<=100):
        print("good job")
    elif(a>=50):
        print("nice")
    else:
        print("bad")

i=0
while i==0:
    a=int(input("Enter the battery in percentage:"))
    if(a<=100):
        battery(a)
    else:
        print("invalid entry")
        break