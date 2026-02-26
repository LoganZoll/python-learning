
print("Student Grade Report")
print("What is your first name")

first_name = input()

print("What is your last name")

last_name = input()

print("It's important the scores are in a form of percentages. Otherwise this program does not work as intended")
print("Input in three different exam scores on different lines")

score1 = float(input())
score2 = float(input())
score3 = float(input())

average = (score1+score2+score3)/3
#Everything before this is old code to find the average of 3 exam


print ("\n\n\n")
print("/\\"*19)
print("\tSTUDENT GRADE REPORT")
print("\\/"*19)
print("Name: " + first_name +" " +last_name)
print(f"Exam 1: {score1}")
print(f"Exam 2: {score2}")
print(f"Exam 3: {score3}")
print("--"*11)
print(f"Average: {average:.2f}")

#Prints grade status
status = ""
if(average>=90):
    status = "Deans List"
elif(average >=70):
    status = "Good Standing"
elif(average>=60):
    status = "Academic Probation"
else:
    status = "Academic Suspension"
print("Status :"+status)



print("/\\"*19)
print ("\tSTUDENT GRADE REPORT")
print("\\/"*19)

#Everything before this is just old code to create a banner
