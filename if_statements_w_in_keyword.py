movies_watched = {"The Matrix", "Green Book", "Her"} #a set containing variables

user_movie = input("Enter something you've watched recently: ") #input asking user if variable is in set

if user_movie in movies_watched: #when python reaches this line it will evaluate the boolean to see if this statement is true
    print(f"I've watched {user_movie} too!") #indented to show it is inside the if statement
else:
    print("I haven't watched that yet.")