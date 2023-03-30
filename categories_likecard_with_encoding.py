import json

# Define a function to read each line of a file with a given encoding
def read_lines(filename, encoding):
    # Open the file with the given encoding
    with open(filename, "r", encoding=encoding) as f:
        # Loop through each line
        for line in f:
            # Yield the line
            yield line

# Define a function to parse each line of json data and check for conditions
def parse_lines(lines):
    # Initialize an empty list to store the categoryIds
    categoryIds = []
    # Initialize a variable to store the current line number
    line_number = 0
    # Loop through each line
    for line in lines:
        # Increment the line number by 1
        line_number += 1
        # Try to parse the json data from the line
        try:
            data = json.loads(line)
            # Check if it is a response object with data field 
            if "response" in data and "data" in data:
                # Loop through each category in the data field 
                for category in data["data"]:
                    # Check if it is a category object 
                    if "id" in category and "categoryParentId" in category and "childs" in category:
                        # Check if it meets the conditions 
                        if category["categoryParentId"] != "0" and has_empty_childs(category):
                            # Add the categoryId to the list 
                            categoryIds.append(category["id"])
        # If an error occurs, print it along with the line number and output 
        except Exception as e:
            print(f"Error at line {line_number}: {e}")
            print(f"Line output: {line}")
    # Return the list of categoryIds 
    return categoryIds

# Define a function to recursively check for empty childs (same as before)
def has_empty_childs(category):
    if not category["childs"]:
        return True
    else:
        for child in category["childs"]:
            if not has_empty_childs(child):
                return False
        return True

# Specify an encoding for reading the file (e.g. utf-8)
encoding = "utf-8"

# Read each line of json data from a file with that encoding 
lines = read_lines("categories.json", encoding)

# Parse each line of json data and check for conditions 
categoryIds = parse_lines(lines)

# Print the list of categoryIds 
print(categoryIds)