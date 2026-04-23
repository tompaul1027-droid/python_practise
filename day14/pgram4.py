text=[]
for i in range(10):
    a=input("Enter the word:")
    text.append(a)

freq={}
for i in text:
    if(i in freq):
        freq[i]=freq[i]+1
    else: 
        freq[i]=1
print(freq)
    
