students=[("Arun",[20,30]),("Maya",[58,40]),("blimly",[89,50])]
b=[]

for i in range(len(students)):
                print(students[i][0],sum(students[i][1]))
                b.append(sum(students[i][1]))
b.sort(reverse=True)
print("Maximum value:",b[0])
print("Minimum value:",b[len(b)-1])

