def name():
    a=input("enter your name:")
    return a
    

def age():
    b=int(input("enter your age:"))
    print(b)


ls=[]
for i in range(2):
    b=name()
    ls.append(b)
    
print(ls)    
