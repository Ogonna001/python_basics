student_info = {
        "name":"Bola Tinubu",
        "age":"20",
        "grade":"C",
        "subjects": ["Math", "Physics", "Chemistry"],
        "address": {"city":"Lagos", "country":"Nigeria"}
        }
print(student_info["name"])
print(student_info.get("age"))
print(student_info["subjects"])
print(student_info["address"])
student_info["grade"] = "A"
print(student_info)
student_info["GPA"] = 4.5
print(student_info.get("GPA"))
student_info.update({"age":21,"school":"OAU"})
print(student_info)
del student_info["GPA"]
print(student_info)
age =student_info.pop("age")
print(student_info)
print(age)
print(len(student_info))
print(student_info.keys())
print(student_info.values())
print(student_info.items())
for key in student_info:
    print(key)

for key,value in student_info.items():
    print(key,value)
