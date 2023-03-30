def describe_pet(type, name):
    print(f"\nI have a {type}")
    print(f"My {type}'s name is {name}")

 #example of positional argument match. python match the order of arguments to function's paratemeter
describe_pet("hamster","Harry")

def describe_pet_2(type,name):
    print(f"\nI have a {type}")
    print(f"My {type}'s name is {name}")

#example of keyword argument explicit match of arguments to parameters
describe_pet_2(type='hamster',name='Anton')

def describe_pet_3(name, type='dog'):
    print(f"\nI have a {type}")
    print(f"My {type}'s name is {name}")

#example of default argument assignment. it should come after empty parameter
describe_pet_3(name='Vova')


def make_shirt(size='L',text='I love Python'):
    print(f"Shirt's size is {size} with the text: \"{text}\"")

make_shirt('M',"I'am special")

make_shirt('M')

make_shirt(text='I learn Python')

#example of simple fuction return
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('Jimmy','Hendrix')
print(musician)


#example of optional return argument
def get_formatted_name_2(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

musician = get_formatted_name_2("Jimmy","Choo")
print(musician)
musician = get_formatted_name_2("Jamie","Curtis","Lee")
print(musician)


#returning a dictionary
def build_person(first_name, last_name, age=None):
    person = {'first_name': first_name, 'last_name': last_name}
    if age:
        person = {'first_name': first_name, 'last_name': last_name, 'age': age}
    return person
person1 = build_person('Jimmy','Lee', 24)
print(person1)

#example of a function with a while loop

def get_formatted_name_3(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print(f"\nPlease, tell me your name:")
    print("enter 'q' at any time to quit")
    f_name = input("First name: ")

    if f_name == 'q':
        break

    l_name = input("Last name: ")

    if l_name == 'q':
        break

    formatted_name = get_formatted_name_3(f_name,l_name)
    print(f"\nHello, {formatted_name}")