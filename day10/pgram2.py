a=int(input("Enter the limit:"))
b=[]
for i in range(a):
    c=int(input("Enter the numbers:"))
    b.append(c)
print(b)
d=[3]
for i in b:
    if(i not in d):
        d.append(i)
print(d)
