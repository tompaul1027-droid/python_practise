a=int(input("Enter the subjects:"))
b=[]
for i in range(a):
    c=int(input("Enter the marks:"))
    b.append(c)
print(b)
b.sort(reverse=True)
print(b)
d=len(b)
print("highest mark:,",b[d-1])
print("lowest mark:",b[0])
print(max(b))
print(min(b))
print(sum(b))
e=sum(b)/a
print(e)