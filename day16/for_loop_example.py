classroom={
    "Alice":{
        "age":14,
        "subject":"Science",
        "Grade":"A"
    },
    "Bob":{
        "age":19,
        "subject":"Maths",
        "Grade":"B"
    }
}
print(classroom.keys())
print(classroom["Alice"]["age"])
for i,j in classroom.items():
    print(i,j)
    if(classroom[i]["age"]>23):
        print(f"{i} is eligable")
    else:
        print(f"{i} is not eligable")