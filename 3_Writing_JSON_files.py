import json

# Example 1 – Write simple dictionary
data = {"name": "Mansur", "age": 18}
with open("data.json", "w") as f:
    json.dump(data, f)

# Example 2 – Write list
numbers = [10, 20, 30]
with open("numbers.json", "w") as f:
    json.dump(numbers, f)

# Example 3 – Write nested data
nested = {"student": {"name": "Ali", "grade": 90}}
with open("nested.json", "w") as f:
    json.dump(nested, f, indent=4)

# Example 4 – Overwrite file
with open("data.json", "w") as f:
    json.dump({"updated": True}, f)

# Example 5 – Write multiple objects (in one structure)
students = [
    {"name": "Ali", "grade": 90},
    {"name": "Sara", "grade": 85}
]
with open("students.json", "w") as f:
    json.dump(students, f, indent=2)