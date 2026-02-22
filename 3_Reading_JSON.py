import json

# Example 1 – Read dictionary
with open("data.json", "r") as f:
    data = json.load(f)
print(data)

# Example 2 – Access value
print(data.get("updated"))

# Example 3 – Read list
with open("numbers.json", "r") as f:
    numbers = json.load(f)
print(numbers)

# Example 4 – Loop through list
for num in numbers:
    print(num)

# Example 5 – Handle missing file safely
try:
    with open("unknown.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found")