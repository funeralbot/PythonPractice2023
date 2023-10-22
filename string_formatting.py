name = "Bob" #normal string
greeting = f"Hello, {name}" #the f-string allows us to embed variables inside a string

print (greeting)

name = "Rolf" #new name for the variable

print(greeting) #still printing first variable

#Solution
name = "Bob"

print(f"Hello, {name}") #instead of using variable as string and printing varaible just print using f-string command

name = "Rolf"

print(f"Hello, {name}") #second string is now displaying new variable


