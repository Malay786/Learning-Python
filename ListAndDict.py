my_list = ["Mercury", "Venus", "Earth"]
print(my_list)
my_list.append("Mars")
print(my_list)
print(my_list[0])

# Dict
student = {
    "name": "Alice",
    "age": "22",
    "Courses": ["Mathematics", "Physics"]
}
# Accessing the value by its key
print(student["name"])
print(student["Courses"][1])

# Modifying a value
student["age"]="20"
print(student["age"])

#Adding a new key-value pair
student["grade"] = "A"
print(student["grade"])
print(student)