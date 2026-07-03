results = {
    "GTA": 90,
     "FC26": 85, 
     "OldGame": 40
 }
for i in list(results):
    if(results[i]<50):
        results.pop(i)
        print(results)
        
     