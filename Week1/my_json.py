import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string into a dictionary
data = json.loads(json_string)
print(data["name"])  # Output: John
