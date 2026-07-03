a=int(input("Enter the limit:"))
b=[]
for i in range(a):
    c=input("Enter the color names:")
    b.append(c)
print(b)
b[1]="yellow"
print(b)
b.append("purple")
print(b)
b .remove("red")
print(b)