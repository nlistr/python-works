# Assign a multi-line string to a variable
text = """Food 3
Food6
Food 5
Food 4
Food8
4Grilled Snd +2 F.F + 2 Pepsi Cans
TestArchive4
2Grilled Snd + 1 F.F + 1 Pepsi Cans
Cocktail+G
Cocktail
Eggplant Yatem"""

# Split the string by new lines and convert it into a list
text_list = text.split("\n")

# Initialize an empty list
text_tuple = []

# Loop through each element in the list
for string in text_list:
    # Strip new lines from the string
    string = string.strip()
    # Append the string to the tuple
    text_tuple.append(string)

# Convert the list into a tuple
text_tuple = tuple(text_tuple)

# Print the tuple
print(text_tuple)