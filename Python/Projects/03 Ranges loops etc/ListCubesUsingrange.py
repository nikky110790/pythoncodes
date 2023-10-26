
# for i in range(1, 101, 1):
#     print("The cube of {0:3} is {1:7}".format(i, i ** 3))

import json

cube = lambda a : a ** 3

print(cube(2))

json_string = '''
{
  "students": [
    {
      "name": "Millie Brown",
      "active": true,
      "rollno": 11
    },
    {
      "name": "Sadie Sink",
      "active": true,
      "rollno": 10
    }
  ]d
}
'''

print(json_string)
print("The type of object is: ", type(json_string))
stud_obj = json.loads(json_string)
print(stud_obj)
print("The type of object is: ", type(stud_obj))
json_obj = json.dumps(stud_obj)
print(json_obj)
print("The type of object is: ", type(json_obj))
