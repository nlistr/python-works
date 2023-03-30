import json

# read in the original JSON structure from file or as a string
with open('import-menu.json', 'r') as f:
    original_json = json.load(f)

# set variables for number of copies
num_option_copies = 2
num_product_copies = 3
num_schedule_copies = 4

# increment integer values in specified keys and create new JSON structure
new_json = {
    'productOptions': [],
    'products': [],
    'schedules': []
}

for i in range(num_option_copies):
    for option in original_json['productOptions']:
        new_key = option['productOptionKey'].split('_')[0] + '_' + str(int(option['productOptionKey'].split('_')[1]) + i + 1)
        option['productOptionKey'] = new_key
        option['nameEn'] = new_key
        option['nameAr'] = new_key
        option['titleEn'] = new_key
        option['titleAr'] = new_key
        for value in option['optionValues']:
            new_key = value['optionValueKey'].split('_')[0] + '_' + str(int(value['optionValueKey'].split('_')[1]) + i + 1)
            value['optionValueKey'] = new_key
            value['nameEn'] = 'Value_' + str(int(value['optionValueKey'].split('_')[1]))
            value['nameAr'] = 'Value_' + str(int(value['optionValueKey'].split('_')[1]))
        new_json['productOptions'].append(option)

for i in range(num_product_copies):
    for product in original_json['products']:
        new_key = product['productKey'].split('_')[0] + '_' + str(int(product['productKey'].split('_')[1]) + i + 1)
        product['productKey'] = new_key
        product['nameEn'] = 'Food_' + str(int(new_key.split('_')[1]))
        product['nameAr'] = 'Food_' + str(int(new_key.split('_')[1]))
        product['descriptionEn'] = 'Food_' + str(int(new_key.split('_')[1]))
        product['descriptionAr'] = 'Food_' + str(int(new_key.split('_')[1]))
        new_json['products'].append(product)

for i in range(num_schedule_copies):
    for schedule in original_json['schedules']:
        new_key = schedule['scheduleKey'].split('_')[0] + '_' + str(int(schedule['scheduleKey'].split('_')[1]) + i + 1)
        schedule['scheduleKey'] = new_key
        new_json['schedules'].append(schedule)

# write out the new JSON structure to file or as a string
with open('new.json', 'w') as f:
    json.dump(new_json, f, indent=4)
