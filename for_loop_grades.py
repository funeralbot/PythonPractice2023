grades = [35, 67, 98, 100, 100]

total = 0

amount = len(grades)

for grade in grades: #create a new variable for grades with grade with a for loop
    total += grade #addes total and grade and returns it to the total, (total = total + grade)

print(total / amount) #print out the average by dividing the total by the amount

grades = [35, 67, 98, 100, 100]#same code with no for loop

total = sum(grades)

amount = len(grades)
print(total / amount)