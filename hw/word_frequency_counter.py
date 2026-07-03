text=input("Enter the sentence:")
text=text.split()
frequency={}
for i in text:
    if(i in frequency):
        frequency[i]=frequency[i]+1
    else:
        frequency[i]=1
print(frequency)