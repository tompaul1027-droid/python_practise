# create a function doorlock  if pin is 1234  door opened otherwise access denied
def doorlock(a):
    if(a==1234):
        print("door opened")
        return 1
    else:
        print("access denied")
        return 2


sum=0
i=0
while i==0:
    a=int(input("Enter the password:"))
    c=doorlock(a)
    if c==1:
        break
    elif(c==2):
        sum=sum+c
        if(sum==6):
            print("bye bye hacker")
            break