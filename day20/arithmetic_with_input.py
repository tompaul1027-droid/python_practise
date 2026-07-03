def bmi(a,b):
    return a/(b**2)



a=int(input("Enter your weight in kg:"))
b=float(input("Enter your height in m:"))
calorie=  bmi(a,b)
print(calorie)