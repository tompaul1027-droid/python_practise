def fruits(*args,**kwargs):
        return args,kwargs,0
a=input("Enter your name:")
b=int(input("Enter your age:"))
c,d,e=fruits(a,b,a=b)
print(e) 