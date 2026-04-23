
#Exercise 1

rgb_color = (255, 128, 0)
print(f"Red:   {rgb_color[0]}")
print(f"Green: {rgb_color[1]}")
print(f"Blue:  {rgb_color[2]}")

palette = []
palette.append(rgb_color)
print(f"{palette}")




#Exercise 2

student1 = ("Alice", 84, 20)
student2 = ("Bob", 96, 21)
student3 = ("Charlie", 40, 19)

classroom = [student1, student2, student3]

print(f"name: {classroom[1][0]}")

name, grade, age = classroom[0]
print(f"Student 1 {name}\n Grade: {grade}, Age: {age}")






#Exercise 3

student = ("Logan", [90, 92, 80], 87.33)
print(f"Original: {student}")

student[1].append(95)

new_student = (student[0], student[1], round(sum(student[1])/len(student[1]),2))
print(f"New: {new_student}")




#Exercies 4

#List so they aren't permanent
grades = [85, 70, 92]

#date because it shouldn't change with time
date = (4, 22, 2026) 

def boost_grades(grades):
    for i in range(len(grades)):
        grades[i] += 5

boost_grades(grades)
print(f"{grades}")






#Exercise 5

def find_range(*numbers):
    return (min(numbers), max(numbers))

print(find_range(10, 55, 33))
print(find_range(4, 88, 23, 67, 12, 99, 45))

test_scores = [78, 92, 85, 88, 91]
print(find_range(*test_scores))








#Exercise 6

def calculate_statistics(*args):
    return (len(args), sum(args), round(sum(args)/len(args), 2))

def update_student_records(records, bonus):
    updated = []
    for name, grade in records:
        updated.append((name, grade + bonus))
    return updated

print(calculate_statistics(85, 90, 78, 92, 88))

students = [("Alice", 85), ("Bob", 72), ("Charlie", 91)]
print(update_student_records(students, 5))









#Exercise 7
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(grid)
print(grid[1][1])

for i in grid:
    for a in i:
        print(f"{a}", end=" ")
    print()









#Exercise 8


student_scores = [45, 78, 92, 61, 88, 73, 55, 90, 82]

passing_grades = [score for score in student_scores if score >= 60]

letter_grades = ['A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' for score in passing_grades]

print(passing_grades)
print(letter_grades)










#Exercise 9
table = [[i * a for a in range(1, 5)] for i in range(1, 5)]

for i in table:
    print(i)

def sum_diagonal(table):
    return sum(table[i][i] for i in range(len(table)))

print(sum_diagonal(table))

even_gen = (val for row in table for val in row if val % 2 == 0)

count = 0
for val in even_gen:
    print(val)
    count += 1
    if count == 5:
        break
