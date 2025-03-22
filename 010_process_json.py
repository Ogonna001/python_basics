import json
with open("009_data.json","r") as my_json:
    car_variable=json.load(my_json)
print(car_variable)
print(car_variable["brand"])
print(car_variable.get("year"))
print(car_variable["features"])
print(car_variable["engine"]["horsepower"])
car_variable["year"] = 2025
print(car_variable)
car_variable.update({"speed":"180km/h"})
print(car_variable)
car_variable.update({"country":"Japan"})
print(car_variable)
del car_variable["color"]
print(car_variable)
model=car_variable.pop("model")
print(car_variable)
print(model)
import json
with open("011_new_data.json","w") as new_json:
    json.dump(car_variable,new_json)
print(car_variable)
print(len(car_variable))
print(car_variable.keys())
print(car_variable.values())
print(car_variable.items())
for key in car_variable:
    print(key)
for key,value in car_variable.items():
    print(key,value)


