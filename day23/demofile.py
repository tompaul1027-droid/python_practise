f=open("file.txt","rt")
a=(f.read())
if "f" in a:
    print("f is in a")
count=0
for i in a:
    if(i=="f"):
        count=count+1
print(f"there are {count} f's in this file")
for i in a:
    print(i)