input_names = input("Enter the names followed by a comma: ")

try:
    # Evaluate for errors in user input, like an extra space.
    filter_names = (i for i in input_names if i != ' ')
    filter_names = ''.join(list(filter_names))

except:
    # Just in case
    print("Problem with iteration")

finally:
    # Split the names into a list by removing the comma
    name_list = filter_names.split(",")

    # Evaluate for errors in capitalization
    func_names = lambda name: (name.lower()).capitalize()

    # Map all names of he list
    mapped = map(func_names, name_list)

    # Turn it back to a list
    new_name_list = list(mapped)

    print(new_name_list)