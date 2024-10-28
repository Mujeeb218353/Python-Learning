print("Find Your Percentage, Total Marks and Grade")

subject_1_marks = int(input("Enter subject 1 marks: "))
subject_2_marks = int(input("Enter subject 1 marks: "))
subject_3_marks = int(input("Enter subject 1 marks: "))
total_marks = subject_1_marks + subject_2_marks + subject_3_marks
percentage = (total_marks/300)*100
grade = ""

if percentage >= 90:
    grade = "A+"
elif 80 <= percentage < 90:
    grade = "A"
elif 70 <= percentage < 80:
    grade = "B"
elif 60 <= percentage < 70:
    grade = "C"
elif 50 <= percentage < 60:
    grade = "D"
else:
    grade = "F"

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)