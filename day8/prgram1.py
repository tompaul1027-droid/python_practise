a=int(input("Enter the limit:"))
b=[]
for i in range(a):
    c=int(input("Enter the  number:"))
    b.append(c)
print(b)
e=[]
d=float(input("Enter the tax rate:"))
d=d/100+1
for i in b:
    i=i*d
    e.append(round(i,3))
    sum=i+sum
print(e)
print("sum=",sum)


