day_of_week = input("What day of the week is it today? ").lower() #the lower command turns all strings into lowercase

print(day_of_week == "Monday")

if day_of_week == "monday": #after a colon defines a block of code indentation is needed after
    print("Have a great start to your week!") #be consistant about indentation
elif day_of_week == "tuesday":#chained if statement; an if statement with three different branches
    print("It's Tuesday.")
else:
    print("Full speed ahead!")

print("This codes always runs") #because it is not in the if statement