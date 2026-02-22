# JSON syntax examples (valid JSON format as strings)

# Example 1 – JSON Object
json_obj = '{"name": "Mansur", "age": 18}'
print(json_obj)

# Example 2 – JSON Array
json_array = '["apple", "banana", "cherry"]'
print(json_array)

# Example 3 – Nested JSON
nested_json = '''
{
    "student": {
        "name": "Ali",
        "grades": [90, 85, 88]
    }
}
'''
print(nested_json)

# Example 4 – JSON with boolean and null
json_special = '{"active": true, "score": null}'
print(json_special)

# Example 5 – Invalid JSON example (single quotes )
invalid_json = "{'name': 'Ali'}"  # JSON requires double quotes
print(invalid_json)