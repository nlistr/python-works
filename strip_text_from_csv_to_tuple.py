# Import csv module
import csv

# Open csv or txt file in read mode
with open("text.txt", "r") as f:
    # Create a csv reader object
    reader = csv.reader(f)
    # Initialize an empty list
    text_list = []
    # Loop through each row in the file
    for row in reader:
        # Get the first element of the row as a string
        string = row[0]
        # Strip new lines from the string
        string = string.strip("\n")
        # Append the string to the list
        text_list.append(string)
    # Convert the list into a tuple
    text_tuple = tuple(text_list)
    # Print the tuple
    print(text_tuple)