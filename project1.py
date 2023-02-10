student_scores = []
while(True):
    grade = input('enter testscores and say "done" to calculate the grades: ')
    if grade == "done":
        break
    student_scores.append(float(grade))

def calculate_grades(scores):
  grades = []
  for score in scores:
    if score >= 90:
      grades.append("A")
    elif score >= 85:
      grades.append("B")
    elif score >= 50:
      grades.append("C")
    else:
      grades.append("F")
  return grades

def calculate_average(scores):
  return round(sum(scores) / len(scores))

student_grades = calculate_grades(student_scores)
class_average = calculate_average(student_scores)

print("Student scores:", student_scores)
print("Student grades:", student_grades)
print("Class average score:", class_average)

