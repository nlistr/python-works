person = {
    "age": 34,
    "first_name": "Jake",
    "last_name": "Sullivan",
    "city": "Washington",
}

#accessing values in dictionary
print(person["age"])

favourite_numbers = {
    "Sarah": 32,
    "John": 3,
    "Michael": 5,
    "Ilya": 7,
    "Nika": 7
}

#looping through keys and values in dictionary
for k,v in favourite_numbers.items():
    print(f"\n{k.title()}'s favourite number is: {v}")

#looping through all the keys in dictionary explicitly using keys method
for name in favourite_numbers.keys():
    print(f"\n{name.title()}")

#looping through all the keys in alpabetical order
for name in sorted(favourite_numbers):
    print(f"\n\tThis is sorted keys order: {name.title()}")

#default looping through keys in dictionary
for name in favourite_numbers:
    print(name)

#looping through values in dictionary
for number in favourite_numbers.values():
    print(f"\n{number}")

#looping through unique values in dictionary, by using set
for number in set(favourite_numbers.values()):
    print(f"\n{number}")


#if-else logic, using dictionary and list
favoutite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

poll_list = [
    "ivan",
    "phil",
    'jessica',
    'mark'
]

for participant in poll_list:
    if participant in favoutite_languages.keys():
        print(f"{participant.title()}, thank you. You already took the poll")
    else: print(f"{participant.title()}, please take a poll")
    

