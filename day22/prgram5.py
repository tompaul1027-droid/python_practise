import cmath
a=[1,2,3,4]
b=list(map(lambda x:x*2,a))
print(b)
mysqr=a[3]**0.5
print(mysqr)
c=[1,2,3,4]
d=sum(b)/len(a)
e=(sum(a)/len(a))**2
f=d-e
g=cmath.sqrt(f)
print(g)
