a=int(input("Enter the limit:")) #the limit of numbers
b=[] #creating a new list
for i in range(a):
    c=int(input("Enter the numbers:")) #the data inside the list
    b.append(c) #adding the data into the new list
print(b)
d=int(input("which number i want to check :")) #which number i want to check which has repeated n times
count=0 #starting value
for i in b:
    if(i==d): #checking whether i has the same values as data inside the new list
        count=count+1 #adding plus 1 to every count of the same number
print(d,"has repeated" ,count ,"times" ) 