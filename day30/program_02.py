a=(input("Enter the Fruit:"))
fruit=["apple","orange","bananna","grapes"]
if(a in  fruit):
    print("already there")
else:
    fruit.append(a)
    print(fruit)