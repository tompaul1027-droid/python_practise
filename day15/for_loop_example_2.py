text=input("Enter the word:")
text=text.split()
print(type(text))
freq={}
for i in text:
    if(i in freq):
            freq[i]=freq[i]+1
    else:
          freq[i]=1
print(freq)


