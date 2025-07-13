student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
## Create the empty student_grades dictionary
student_grades = {}
# student_grades = input("Enter the student score")
for key in student_scores:
    score = student_scores[key]
    if 91 <= student_scores[key] <= 100:
        student_scores[key] = str("Outstanding")
    elif 81 <= student_scores[key] <= 90:
        student_scores[key] = str("excellent")
    elif 71 <= student_scores[key] <= 80:
        student_scores[key] = str("Good")
    elif student_scores[key] <= 70:
        student_scores[key] = str("Fail")
    else:
        break
    student_grades.update(student_scores)

print(student_grades)