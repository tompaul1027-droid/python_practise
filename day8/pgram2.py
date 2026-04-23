a=int(input("Enter the limit:"))
b=[]
for i in range(a):
    c=int(input("enter the number:"))
    b.append(c)
print(b)
count=0
for i in b:
    if(i<=2000):
        count=count+1
print(count)


