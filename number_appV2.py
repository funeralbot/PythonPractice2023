number = 7 #hidden number from user



while True: #infinate loop of guess number game
    user_input = input("Would you like to play? (Y/n)")  # input asking if user wants to play

    if user_input == "n": #end the loop from inside the game
        break

    user_number = int(input("Guess the number: ")) #input asking for number
    if user_number == number:
        print("You guess correctly!") #victory output
    elif abs(number - user_number) == 1: #using absolute value to see how far off the user was from the number
        print("You were off by one.")
    else:
        print("Sorry, it's wrong!") #failure output

