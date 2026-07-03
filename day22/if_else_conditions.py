def fact(a):
    if(a==1):
        return a
    else:
        return a*fact((a-1))

a=int(input("Enter the number:"))
b=fact(a)
print(b)