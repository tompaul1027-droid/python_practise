car={
    "brand": "bmw",
    "color":"black",
    "price":"$150000",
    "number plate":"KL07TP1027"
}
print(car.items())
car["engine"]="V16"
print(car)
car.update({"tyre":"Goodyear"})
print(car)
car.update({"color":"blue"})
print(car)
car["color"]="black" 
print(car) 