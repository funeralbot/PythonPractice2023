#size_input = input("How big is your house (in square feet): ") #the input function will always give you a string

#square_meters = size_input / 10.8 #unsupported operamd error because size input is a string and 10.8 is a float

#print(square_meters #unable to display information because two of the two different data types


size_input = input("How big is your house (in square feet): ") #the input function will always give you a string

square_feet = int(size_input) #pass the size_input variable through an integer conversion function

square_meters = square_feet / 10.8 #use the new integer variable to convert square feet to meters

print(square_meters) #display square meters to the user

print(f"{square_feet} square feet is {square_meters:.2f} square meters.") #display the information to the user using the F string command
#as well as truncate the output to only two decimal places using :.2f
