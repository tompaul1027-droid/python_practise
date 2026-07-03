def fruits(*args,**kwargs):
        return args,kwargs
a,b=fruits("apple","mango","orange",price=20,name="thomas")
print(a,b)