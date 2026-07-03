a=int(input("Enter the limit:"))
b=[]
for i in range(a):
    c=int(input("Enter the numbers:"))
    b.append(c)
print(b)
b=tuple(b)
sum=0
for i in b:
    sum=sum+i
print(sum)
print(type(b))