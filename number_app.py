number = 7 #hidden number from user

user_input = input("Enter 'y' if you would like to play: ") #input asking if user wants to play

if user_input == "y": #if statement for game logic
    user_number = int(input("Guess the number: ")) #input asking for number
    if user_number == number:
        print("You guess correctly!") #victory output
    else:
        print("Sorry, it's wrong!") #failure output