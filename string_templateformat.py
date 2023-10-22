name = "Bob" #variable with string

greeting = "Hello, {}" #gretting string used as template

with_name = greeting.format(name) #calls the format function inside the gretting variable giving a name to the template

with_name_two = greeting.format("Rolf") #template with a new name, instead of using variable, using string directly


print(with_name) #prints greeting string with name variable

print(with_name_two) #greeting template with new name