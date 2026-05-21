import math
def fact(n,r):
    c=math.factorial(n)
    d=math.factorial(r)
    e=math.factorial(n-r)
    return c/(d*e)









a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
n=int(input("Enter the limit:"))
sum=0
for i in range(n):
    f=fact(n,i)
    g=a**(n-i)
    h=b**i
    j=f*g*h
    sum=sum+j

print(sum)
