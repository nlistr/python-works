import json

with open("data.json") as json_file:
    json_data = json.load(json_file)

print(len(json_data))
