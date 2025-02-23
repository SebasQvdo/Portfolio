# lambda λ, mapped and filtered functions
x_value = range(1, 10) # Create a range of #s for x
func_y = lambda x : x**2


# Iterate every value of the range into the function and output it as a readable list
mapped_y = list( map(func_y, x_value) )

print(mapped_y)



# Filtered functions, instead of returning booleans, they return the values that are True
func_bool = lambda nums : nums%2 == 0
evens_map = list( map(func_bool, mapped_y) )
evens_filter = list( filter(func_bool, mapped_y) )

print(evens_map) # Displays the return boolean value
print(evens_filter) # Displays value if it is True



# Examples
#Managing budget
prices = {
    "MacBook": 1200,
    "eMachines": 500,
    "Windows": 850,
    "HP": 700,
    "Lenovo": 650
}

budgets = dict( filter( lambda price : price[1] <= 800 , prices.items() ) )

print(budgets)

#Cleaning data
answers = ["Yes", "", "No", "Maybe", "", "Yes",]

filtered_answers = list( filter( lambda ans : ans != "" , answers ) )

print(filtered_answers)
