student={"id":1,"name":"Peteru","gender":"Male","department":"Comp Sci","school":"Unilag",}


import json
with open("013_data.json","w") as my_file:
    json.dump(student,my_file)
print(student)
