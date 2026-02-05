print("Student Exam Average Calculator")
print("What is your first name")

first_name = input()

print("What is your last name")

last_name = input()

print("It's important the scores are in a percentage of the points, or all exams were worth the same amount of points if you want this to accurately portray your averages scores")
print("Input in three different exam scores on different lines")

score1 = float(input())
score2 = float(input())
score3 = float(input())

print(first_name + " " + last_name +", your average of the three exams comes out to " + str(round((score1 + score2 + score3) / 3, 2)) + " points")