import json

# Example 1 – Parse simple JSON
data = '{"name": "Mansur", "age": 18}'
parsed = json.loads(data)
print(parsed)
print(parsed["name"])

# Example 2 – Parse JSON array
arr = '["apple", "banana", "cherry"]'
parsed_arr = json.loads(arr)
print(parsed_arr[1])

# Example 3 – Parse nested JSON
nested = '{"student": {"name": "Ali", "grade": 90}}'
parsed_nested = json.loads(nested)
print(parsed_nested["student"]["grade"])

# Example 4 – JSON with boolean
bool_json = '{"active": true}'
print(json.loads(bool_json)["active"])

# Example 5 – JSON with null
null_json = '{"score": null}'
print(json.loads(null_json)["score"])