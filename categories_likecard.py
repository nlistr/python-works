import json

def parse_json(json_data, category_ids):
    for category in json_data['data']:
        if category['categoryParentId'] != "0" and category['childs'] == []:
            category_ids.append(category['id'])
        if category['childs'] != []:
            parse_json({'data': category['childs']}, category_ids)

with open('categories.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

category_ids = []
parse_json(json_data, category_ids)
print(category_ids)
print("\nNumber  of the categories:", len(category_ids))