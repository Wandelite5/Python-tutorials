# Write a grading application that will read a list of student scores, Output the different grades and print out 
# the class average score 
print("Enter scores obtained in 6 subjects: ")
student_score1 = int(input())
student_score2 = int(input())
student_score3 = int(input())
student_score4 = int(input())
student_score5 = int(input())
student_score6 = int(input())

total_score = student_score1 + student_score2 + student_score3 + student_score4 + student_score5 + student_score6
class_average = round(total_score/6)

# Grade A: >= 90
# Grade B: >= 85 and < 90
# Grade C: >= 50 and <85
# Grade F:  < 50

if class_average >= 90:
    print("Your Grade is A")
elif class_average >= 85 and class_average < 90:
    print("Your Grade is B")
elif class_average >= 50 and class_average < 85:
    print("Your Grade is C")
else:
    print("Your Grade is F")

print("Your class average is {}".format(class_average))

