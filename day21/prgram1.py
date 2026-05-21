# create a function doorlock  if pin is 1234  door opened otherwise access denied
def doorlock(a):
    if(a==1234):
        print("door opened")
    else:
        print("access denied")



a=int(input("Enter the password:"))
doorlock(a)
