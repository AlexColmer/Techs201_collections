# # Dictionaries
#
# # just another way to manage data in python little more complex. they wrok with key/value pairs
# # key = a reference to a particular object
# # value = data storage mechanism you want to use
#
# # Create a dictionary
#
# student_1 = {
#     "name": "Susan",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lesson_names": ["Variables", "data_types", "set_up"]
#
# }
#
# print(student_1["stream"])
#
# # access element of the list
# print(student_1["completed_lesson_names"][2])
#
# # changing a value in a dictionary
# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
#
# #removing from a dictionary
#
# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])
#
# #dictianroy methods
#
# #Keys
# print(student_1.keys())
# #get values of a key back without []
# print(student_1.get("name"))
# #get values of a dictionary
# print(student_1.values())
# #prints the key/value pairs
# print(student_1.items())


student_2 = {
    "School": "Sparta global",
    "Subject": "Python",
    "Extra curricular": ["basketball", "art", "Photography"],
    "lessons in a day": 5,
    "hours in a day": 12.5
}

print(student_2.items())
student_2["lessons in a day"] = 4
print(student_2)