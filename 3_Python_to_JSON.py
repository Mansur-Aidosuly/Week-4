import json

# Example 1 – Convert dictionary
data = {"name": "Mansur", "age": 18}
json_string = json.dumps(data)
print(json_string)

# Example 2 – Convert list
numbers = [1, 2, 3, 4]
print(json.dumps(numbers))

# Example 3 – Pretty printing
print(json.dumps(data, indent=4))

# Example 4 – Sorting keys
print(json.dumps(data, indent=2, sort_keys=True))

# Example 5 – Convert complex structure
complex_data = {
    "students": [
        {"name": "Ali", "grade": 90},
        {"name": "Sara", "grade": 85}
    ]
}
print(json.dumps(complex_data, indent=4))